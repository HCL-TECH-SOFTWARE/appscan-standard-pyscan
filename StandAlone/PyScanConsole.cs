/*#######################################################################################################################
# Licensed Materials –Property of HCL Technologies Ltd.
# © Copyright HCL Technologies Ltd. 2022.
# All rights reserved. See product license for details. US Government Users Restricted Rights. Use, duplication,
# or disclosure restricted by GSA ADP Schedule Contract with HCL Technologies Ltd. Java and all Java-based trademarks
# and logos are trademarks or registered trademarks of Oracle and/or its affiliates. HCL, the HCL logo,
# and Tivoli are registered trademarks of HCL Technologies in the United States, other countries, or both.
#######################################################################################################################*/

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
