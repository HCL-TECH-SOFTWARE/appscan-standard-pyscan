#
# runs explore, excludes all paths, and runs test (supposed to be a short test..)
#

def ExcludeNode(node):
    conf.PathFilters.Exclude(node.Path)
    for n in node.Children:
        ExcludeNode(n)


# execfile("_defs.py")
from _defs import *

scan.Scan(1, 0)

ExcludeNode(sdata.AppTreeRoot)

scan.Scan(0, 1)
