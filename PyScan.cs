//#######################################################################################################################
//# Licensed Materials �Property of HCL Technologies Ltd.
//# � Copyright HCL Technologies Ltd. 2022.
//# All rights reserved. See product license for details. US Government Users Restricted Rights. Use, duplication,
//# or disclosure restricted by GSA ADP Schedule Contract with HCL Technologies Ltd. Java and all Java-based trademarks
//# and logos are trademarks or registered trademarks of Oracle and/or its affiliates. HCL, the HCL logo,
//# and Tivoli are registered trademarks of HCL Technologies in the United States, other countries, or both.
//#######################################################################################################################

using System;
using System.IO;
using System.Reflection;
using System.Threading;
using Python.Runtime;
using AppScan;
using AppScan.Extensions;
using ThreadState = System.Threading.ThreadState;
using TraceLevel = System.Diagnostics.TraceLevel;

namespace PyScan
{

    public enum PyScanActionValues
    {
        NoAction = 0,
        OpenIdle = 1,
        Quit = 2
    }

    public static class PyScanAction
    {
        private static PyScanActionValues action = PyScanActionValues.NoAction;

        public static int Get()
        { return (int)action; }

        public static void Set(int value)
        { Set((PyScanActionValues)value); }

        public static void Set(PyScanActionValues value)
        { action = value; }
    }

    /// <summary>
    /// PyScan main implementation class.
    /// implementing the IExtensionLogic interface
    /// </summary>
    public class PyScan : IExtensionLogic, IDisposable
    {

        /// <summary>
        /// extension initialization. typically called on AppScan's startup
        /// </summary>
        /// <param name="appScan">main application object the extension is loaded into</param>
        /// <param name="extensionDir">extension's working directory</param>
        public void Load(IAppScan appScn, IAppScanGui appScanGui, string extensionDir)
        {
            appScan = appScn;
            cDllErrorMessage = TStrings.Instance.GetString("PyScan.dllErrorMessage");
            IMenuItem<EventArgs> menuCommand = new MenuItem<EventArgs>(TStrings.Instance.GetString("PyScan.StartPyScan"), PyScanMain);
            appScanGui.ExtensionsMenu.Add(menuCommand);
            IappScanGui=appScanGui;
        }

        private void PyScanMain(EventArgs args)
        {
            // init PythonEngine if necessary
            try
            {
                if (!PythonEngine.IsInitialized)
                {
                    PythonEngine.Initialize();
                }
            }
            catch (SystemException e) when (e is DllNotFoundException || e is BadImageFormatException)
            {
                if (cDllErrorMessage == String.Empty)
                    cDllErrorMessage = TStrings.Instance.GetString("PyScan.dllErrorMessage");
                Console.WriteLine(e.ToString());
                IappScanGui.ShowMessageBox("PyScan extension", "Error", ExtensionsApiMessageBoxButtons.OK, ExtensionsApiMessageBoxSeverity.Error);
                return;
            }

            // init PyScan:
            Init();

            // set the flag, so the thread knows it should open IDLE window
            PyScanAction.Set(PyScanActionValues.OpenIdle);

            // run IDLE in a new thread:
            if ((pythonThread == null) || (!IsRunning()))
            {
                StartPython_NewThread();
            }
        }

        void StartPythonImpl()
        {
            try
            {
                // run the script:
                string[] cmd = new string[2] { "python", scriptFileName };
                object o = Runtime.Py_Main(cmd.Length, cmd);
            }
            catch
            {
            }
        }

        #region threading

        void StartPython_NewThread()
        {
            pythonThread = new Thread(new ThreadStart(StartPythonImpl));
            pythonThread.SetApartmentState(ApartmentState.STA);
            pythonThread.IsBackground = true;
            pythonThread.Start();
        }

        bool IsRunning()
        {
            return
                pythonThread.ThreadState == ThreadState.Running ||
                pythonThread.ThreadState == ThreadState.Background;
        }

        private Thread pythonThread;

        #endregion threading

        #region initialization and termination

        void Init()
        {
            if (scriptFileName != null)
            {
                // already initialized
                return;
            }

            // copy init-script to FS
            //////////////////////////////

            // get a temp file:
            scriptFileName = Path.Combine(appScan.AppScanTempDir, "PyScanInit.py");

            // read init script:
            const string resourceName = "PyScan.OpenConsole.py";
            Stream stream = Assembly.GetExecutingAssembly().GetManifestResourceStream(resourceName);
            int len = (int)stream.Length;
            byte[] buff = new byte[len];
            stream.Read(buff, 0, len);

            // write script to the file:
            using (FileStream f = new FileStream(scriptFileName, FileMode.Create, FileAccess.Write))
            {
                f.Write(buff, 0, len);
                f.Flush();
            }

        }

        //Implement IDisposable.
        public void Dispose()
        {
            Dispose(true);
            GC.SuppressFinalize(this);
        }

        protected virtual void Dispose(bool disposing)
        {
            try
            {
                File.Delete(scriptFileName);
            }
            catch
            {
                // do nothing
            }
        }

        // Use C# destructor syntax for finalization code.
        ~PyScan()
        {
            // Simply call Dispose(false).
            Dispose(false);
        }


        #endregion initialization and termination

        #region data members

        private IAppScan appScan;
        private string scriptFileName;
        private IAppScanGui IappScanGui;
        #endregion data members

        #region consts

        private string cDllErrorMessage;

        #endregion consts

        #region other

        /// <summary>
        /// retrieves data about current available ext-version
        /// </summary>
        /// <param name="targetApp">app this extension is designated for</param>
        /// <param name="targetAppVersion">current version of targetApp</param>
        /// <returns>update data of most recent extension version, or null if no data was found, or feature isn't supported. it is valid to return update data of current version. extension-update will take place only if returned value indicaes a newer version</returns>
        public ExtensionVersionInfo GetUpdateData(Edition targetApp, Version targetAppVersion)
        {
            return null;
        }

        #endregion other
    }
}

