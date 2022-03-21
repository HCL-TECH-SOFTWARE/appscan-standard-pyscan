#
# loads a scan, and preforms rescan
#

# execfile("_defs.py")
from _defs import *

filename = lines[1]

scan.LoadScanData(filename)
scan.ReScan(1,0)


