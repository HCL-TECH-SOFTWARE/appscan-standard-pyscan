
In order to run Pyscan standalone:

1. Copy the following files to AppScan's installation dir (typically: C:\Program Files\IBM\Rational AppScan\)
	CLR.dll
	Python.Runtime.dll
	PyScan.exe
	InitPyScan.py

2. Run PyScan.exe

3. Init appScan variable, in order to access AppScan from the PyScan console.
   Do it by running the following command on PyScan console:	
	>>> execfile('InitPyScan.py')
	
4. You can now access AppScan using the appScan variable. for example:
	>>> appScan.Scan.ScanData.Config.StartingUrl 
	
5. In order to execute a script instead of receiving the console, run PyScan.exe myScript.py
   Inside the script you can use execfile('InitPyScan.py') and then access the appScan variable.
	
