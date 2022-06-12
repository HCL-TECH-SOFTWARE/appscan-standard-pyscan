Download Pyscan

https://github.com/HCL-TECH-SOFTWARE/appscan-standard-pyscan

==========================================================

Compile your PyScan extension

Prerequisites:

You must have AppScan installed on your local machine.

If it’s installed in the default folder:
"C:\Program Files (x86)\HCL\AppScan Standard\"
you can skip Step 1.

1) Attach DLLs from AppScan install folder:
	a) Open “PyScan.sln” with Visual Studio.
	b) Locate and right-click on PyScan project.
	c) Click Add > Reference
	d) In the Browse section, select Browse and add the following 2 DLLs from the AppScan folder:
		o	AppScanSDK.dll
		o	AppScanVersionInfo.dll

2) Under project properties you can optionally define the build output location. By default it is the working folder.

3) Click Build and your PyScan extension is created.

===========================================================

Add the PyScan extension to AppScan:

1) In AppScan, go to Tools > Extensions > Extension manager.
2) Click “Add extension from:” button, and select the “PyScanExt.zip” file you created previously.
3) Restart AppScan for the change to take effect.

===========================================================

Use PyScan in Appscan:

1) For best results using the extension it is recommended to configure a Starting URL.
2) Click Tools > Extension > Start Pyscan.
3) From the console that opens do one of the following:
	- Open your Python file or module, and click Run > Run module.
	- Write Python code in the console and run it.

Example
These steps will modify a fuzz word in the demo site requests, which will be printed to the console.
1) In Appscan, open the demo.testfire.com .scan file.
2) Click Tools > Extension > Start Pyscan.
3) From the console menu click File > Open, then locate and select “PyscanUtils.py” file; then click Run > Run Module.
	
