//#######################################################################################################################
//# Licensed Materials –Property of HCL Technologies Ltd.
//# © Copyright HCL Technologies Ltd. 2022.
//# All rights reserved. See product license for details. US Government Users Restricted Rights. Use, duplication,
//# or disclosure restricted by GSA ADP Schedule Contract with HCL Technologies Ltd. Java and all Java-based trademarks
//# and logos are trademarks or registered trademarks of Oracle and/or its affiliates. HCL, the HCL logo,
//# and Tivoli are registered trademarks of HCL Technologies in the United States, other countries, or both.
//#######################################################################################################################

using System;
using System.Collections.Generic;
using System.Text;
using System.Resources;
using System.Reflection;

namespace PyScan
{
    public class TStrings
    {
        private static TStrings stringsInstance = null;
        private static object stringsInstanceLock = new object();
        private ResourceManager localResourceManager;

        private TStrings()
        {
            localResourceManager = new ResourceManager("PyScan.Resources.Strings",
               Assembly.GetExecutingAssembly());
        }

        /// <summary>
        /// Initiate String class 
        /// </summary>
        public static TStrings Instance
        {
            get
            {
                lock (stringsInstanceLock)
                {
                    if (stringsInstance == null)
                    {
                        stringsInstance = new TStrings();                       
                    }
                    return stringsInstance;
                }
            }

        }

        /// <summary>
        /// Returns a specific string from the resources file using an ID. 
        /// </summary>
        /// <param name="resourceId">The resource ID</param>
        /// <returns>The resource file string</returns>
        public string GetString(string resourceId)
        {            
            string resourceManagerString = "";
            resourceManagerString = localResourceManager.GetString(resourceId);
            if (resourceManagerString == null)
                resourceManagerString = "";
            

            return resourceManagerString;
        }
       		
    }
}
