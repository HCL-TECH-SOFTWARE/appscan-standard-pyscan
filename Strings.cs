/******************************************************************
* Licensed Materials - Property of HCL
* (c) Copyright HCL Technologies Ltd. 2008, 2009.
* Note to U.S. Government Users Restricted Rights.
******************************************************************/

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
            localResourceManager = new ResourceManager("PyScan.Strings",
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
