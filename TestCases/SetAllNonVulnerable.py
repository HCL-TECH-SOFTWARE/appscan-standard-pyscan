#######################################################################################################################
# Licensed Materials –Property of HCL Technologies Ltd.
# © Copyright HCL Technologies Ltd. 2022.
# All rights reserved. See product license for details. US Government Users Restricted Rights. Use, duplication,
# or disclosure restricted by GSA ADP Schedule Contract with HCL Technologies Ltd. Java and all Java-based trademarks
# and logos are trademarks or registered trademarks of Oracle and/or its affiliates. HCL, the HCL logo,
# and Tivoli are registered trademarks of HCL Technologies in the United States, other countries, or both.
#######################################################################################################################
#
# runs full test, and sets all issues as non-vulnerable
#

# execfile("_defs.py"
from _defs import *


def NonVulNode(node):
    for n in node.GetIssues():
        sdata.SetAsNotVulnerable(n)
    for n in node.Children:
        NonVulNode(n)


scan.Scan(1, 1)
NonVulNode(sdata.AppTreeRoot)
