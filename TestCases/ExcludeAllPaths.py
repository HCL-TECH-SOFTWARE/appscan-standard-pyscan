#######################################################################################################################
# Licensed Materials –Property of HCL Technologies Ltd.
# © Copyright HCL Technologies Ltd. 2022.
# All rights reserved. See product license for details. US Government Users Restricted Rights. Use, duplication,
# or disclosure restricted by GSA ADP Schedule Contract with HCL Technologies Ltd. Java and all Java-based trademarks
# and logos are trademarks or registered trademarks of Oracle and/or its affiliates. HCL, the HCL logo,
# and Tivoli are registered trademarks of HCL Technologies in the United States, other countries, or both.
#######################################################################################################################
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
