/******************************************************************
* IBM Confidential
* OCO Source Materials
* IBM Rational AppScan Standard Edition
* (c) Copyright IBM Corp. 2007, 2010.
* 
* The source code for this program is not published or otherwise
* divested of its trade secrets, irrespective of what has been
* deposited with the U.S. Copyright Office.
******************************************************************/

using System;
using System.Collections.Generic;
using System.Text;
using Python.Runtime;

namespace PyScan
{
    public sealed class PythonConsole
    {

        private PythonConsole() { }

        [STAThread]
        public static void Main(string[] args)
        {
            string[] cmd = Environment.GetCommandLineArgs();
            PythonEngine.Initialize();

            int ret = Runtime.Py_Main(cmd.Length, cmd);

            PythonEngine.Shutdown();
        }

    }
}
