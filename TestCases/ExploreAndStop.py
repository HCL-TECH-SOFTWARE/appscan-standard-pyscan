#
# runs explore and stops it after 10 seconds
#

# execfile("_defs.py")
from _defs import *
import threading
import time


def StartExplore(a, b):
    scan.Scan(a, b)


threading.Thread(target=StartExplore, args=(1, 0)).start()
time.sleep(10)
scan.Stop()
