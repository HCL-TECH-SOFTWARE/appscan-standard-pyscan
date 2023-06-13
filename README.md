AppScan Standard - PyScan extension

You can download a ZIP file containing the latest PyScan extension release or compile your own.

Prerequisite:
- You must have Python version 3.8 installed on the machine that will run the extension, and Python must be added to the Windows path. 
  To add it: On your machine, in the system Environment Variables > User variables > Path, add a path to your Python installation directory, then restart your machine.

==========================================================

A) Download PyScan extension

The latest version can be found in the GitHub repository, in the Releases section.

1) Click on PyScanExt.zip to download the extension.
2) Add the extension to AppScan as described in section C below.

==========================================================

B) Compile your PyScan extension

Prerequisites:
- You must be able to compile a C# Project.
- You must have 7-zip installed (http://www.7-zip.org/).
- You must have AppScan Standard version 10.1.0 or later.


Skip Step 1 if AppScan Standard is installed in the default folder:
"C:\Program Files (x86)\HCL\AppScan Standard\"

1) Attach DLLs from AppScan install folder:
	a) Open “PyScan.sln” with Visual Studio or other IDE of your choice.
	b) Locate and right-click on PyScan project.
	c) Click Add > Reference
	d) In the Browse section, select Browse and add the following 4 DLLs from the AppScan folder:
		o	AppScanSDK.dll
		o	debug.dll
		o	utilities.dll
		o	AppScanVersionInfo.dll (this file is located in \Tools\Authentication Tester)

2) Under project properties you can optionally define the build output location. By default it is the working folder.

3) Click Build and your PyScan extension is created.

===========================================================

C) Add the PyScan extension to AppScan:

1) In AppScan, go to Tools > Extensions > Extension manager.
2) Click “Add extension from:” button, and select the “PyScanExt.zip” file you created previously or downloaded.
3) Restart AppScan for the change to take effect.

===========================================================

D) Use PyScan in AppScan:

1) If your scripts need a Starting URL and this is not configured in the scan on which you are running the script,
   you must configure it in Scan Configuration > URLs and servers.
2) Click Tools > Extension > Start Pyscan.
3) From the console that opens do one of the following:
	- Open your Python file or module, and click Run > Run module.
	- Write Python code in the console and run it.

Example 1: PyscanFuzzerUtil.py
These steps will modify a fuzz word in the demo site requests, which will be printed to the console.
1) In AppScan, open demo.testfire.net.scant (Starting URL is already configured).
2) Click Tools > Extension > Start Pyscan.
3) From the console menu click File > Open, then locate and select “PyscanFuzzerUtil.py”(in the ZIP file you downloaded), then click Run > Run Module.

Example 2: UserDefinedTests_MultiplePayloads.py
These steps will run your user-defined tests with multiple payloads.
1) In AppScan, open demo.testfire.net.scant (Starting URL is already configured).
2) Click Tools > Extension > Start Pyscan.
3) From the console menu click File > Open, then locate and select “UserDefinedTests_MultiplePayloads.py”(in the ZIP file you downloaded), then click Run > Run Module.

===========================================================
	
E) Use AppScan methods

You can call AppScan SDK methods from your Python script. The SDK documentation is located in your AppScan Docs folder, which by default is:
"C:\Program Files (x86)\HCL\AppScan Standard\Docs\AppScanSDK.chm"

===========================================================
	
 F) License
 
 All files found in this project are licensed under the Apache License 2.0.
