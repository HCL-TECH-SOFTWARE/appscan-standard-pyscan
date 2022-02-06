#
# runs full test, and sets all issues as non-vulnerable
#

from _defs import *


def NonVulNode(node):
    for n in node.GetIssues():
        sdata.SetAsNotVulnerable(n)
    for n in node.Children:
        NonVulNode(n)


scan.Scan(1, 1)
NonVulNode(sdata.AppTreeRoot)
