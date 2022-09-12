#######################################################################################################################
# Licensed Materials –Property of HCL Technologies Ltd.
# © Copyright HCL Technologies Ltd. 2022.
# All rights reserved. See product license for details. US Government Users Restricted Rights. Use, duplication,
# or disclosure restricted by GSA ADP Schedule Contract with HCL Technologies Ltd. Java and all Java-based trademarks
# and logos are trademarks or registered trademarks of Oracle and/or its affiliates. HCL, the HCL logo,
# and Tivoli are registered trademarks of HCL Technologies in the United States, other countries, or both.
#######################################################################################################################
import sys

# make IDLE run in the same process:
sys.argv.append('-n')

# set IDLE window title:
sys.argv.append('-t')
sys.argv.append('Pyscan')

# PyShell user might do things which change sys.argv.
# make a copy of sys.argv, so we can restore it later
origArgv = [x for x in sys.argv]

# set working dir:
try:
	import os
	wd = os.environ['UserProfile']	
	os.chdir(wd)
	os.chdir("My Documents")
	os.chdir("AppScan")		
except:
	pass

# set appScan variable:
import clr
from clr import System
from clr import AppScan
from clr import DBAdapter
from clr import Utilities
appScan = clr.AppScan.AppScanFactory.CreateInstance()

# main loop: open IDLE window:

from idlelib import pyshell
from time import sleep
from clr import PyScan

done = 0
while done == 0:

	#restore orig sys.argv:
	sys.argv = [x for x in origArgv]
	pyshell.main()	
	clr.PyScan.PyScanAction.Set(0)
	
	# wait for env var to change:
	while 1:
		sleep(1.5)
		val = clr.PyScan.PyScanAction.Get()		
		if val == 1:
			break