/******************************************************************
* IBM Confidential
* OCO Source Materials
* IBM Rational AppScan Standard Edition
* (c) Copyright IBM Corp. 2008,2009 All Rights Reserved.
* 
* The source code for this program is not published or otherwise
* divested of its trade secrets, irrespective of what has been
* deposited with the U.S. Copyright Office.
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
