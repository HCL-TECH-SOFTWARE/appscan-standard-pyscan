#######################################################################################################################
# Licensed Materials –Property of HCL Technologies Ltd.
# © Copyright HCL Technologies Ltd. 2022.
# All rights reserved. See product license for details. US Government Users Restricted Rights. Use, duplication,
# or disclosure restricted by GSA ADP Schedule Contract with HCL Technologies Ltd. Java and all Java-based trademarks
# and logos are trademarks or registered trademarks of Oracle and/or its affiliates. HCL, the HCL logo,
# and Tivoli are registered trademarks of HCL Technologies in the United States, other countries, or both.
#######################################################################################################################
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
