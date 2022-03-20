how to compile your own PyScan:

perquisition requirements:

you must have AppScan installed on your local machine.
In case it’s installed on the default folder:
"C:\Program Files (x86)\HCL\AppScan Standard\" you can skip next step.
Additional step in case you’ve got AppScan installed anywhere else:
You’ll need to attach required DLL’s from AppScan install folder:
-	Open “PyScan.sln” with visual studio.
-	Locate and click right click on PyScan project.
-	Click Add->reference
-	Under “browse” section select browse and locate the 2 following DLL’s within installed AppScan folder:
o	AppScanSDK.dll
o	AppScanVersionInfo.dll
Under project properties you can choose build output location (default will be the working folder).
Now you can simply click on build and your very own PyScan extension will be created.

Adding PyScan extension to AppScan:

Open AppScan, under Tools->Extensions->extension manager: 
click on “Add extension from:” button, then locate and choose the “PyScanExt.zip” file.
You’ll now need to restart AppScan before using the extension.

Use PyScan with Appscan:

Usually Pyscan is used to analyze and test results so at the very least it’s recommended to configure a starting URL.
From appscan menu choose: tools->extension->start Pyscan
From the opened window you can choose to open or create python files you which to run, when done writing a python script you can click on “Run”->”Run Module” and your selected script will run.
Demo example:
Within appscan open a demo.testfire.com .scant file.
From appscan menu choose: tools->extension->start Pyscan
From the menu; locate and choose “PyscanUtils.py” file and click on “Run”->”Run Module”.
The following steps if configured correctly will result in a demo fuzz word within the demo site request. This will run and show results on terminal.
