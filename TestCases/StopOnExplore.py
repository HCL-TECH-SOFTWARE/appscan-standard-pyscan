#
# immediately stop explore whenever the user starts it
#

from _defs import *


def StopIt(a,b):
    scan.Stop()


scan.ExploreStarting += StopIt

