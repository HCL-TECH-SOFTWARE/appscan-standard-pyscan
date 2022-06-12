How to compile your own PyScan extension

Prerequisites:

You must have AppScan installed on your local machine.

If it’s installed in the default folder:
"C:\Program Files (x86)\HCL\AppScan Standard\"
you can skip Step 1.

1) Attach DLLs from AppScan install folder:
	-	Open “PyScan.sln” with Visual Studio.
	-	Locate and right-click on PyScan project.
	-	Click Add > Reference
	-	In the Browse section, select Browse and locate the following 2 DLLs within the AppScan folder:
		o	AppScanSDK.dll
		o	AppScanVersionInfo.dll

2) Under project properties you can choose a build output location. Otherwise, by default it is the working folder.

3) Click Build and your PyScan extension is created.

===========================================================

Adding the PyScan extension to AppScan:

1) In AppScan, go to Tools > Extensions > Extension manager.
2) Click “Add extension from:” button, and select the “PyScanExt.zip” file you created previously.
3) Restart AppScan for the change to take effect.

===========================================================

Using PyScan in Appscan:

1) For best results using the extension it is recommended to configure a Starting URL.
2) Click Tools > Extension > Start Pyscan.
3) From the console that opens you can:
	a) Open your Python file or module, and click Run > Run module.
	b) Create Python code in the console and run it.

Example:
1) In Appscan, open the demo.testfire.com .scan file.
2) Click Tools > Extension > Start Pyscan.
3) From the console menu click File > Open, then locate and select “PyscanUtils.py” file; then click Run > Run Module.
	These steps will modify a fuzz word in the demo site requests, which will be printed to the console.
