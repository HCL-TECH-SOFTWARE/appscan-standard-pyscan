#######################################################################################################################
# Licensed Materials –Property of HCL Technologies Ltd.
# © Copyright HCL Technologies Ltd. 2022.
# All rights reserved. See product license for details. US Government Users Restricted Rights. Use, duplication,
# or disclosure restricted by GSA ADP Schedule Contract with HCL Technologies Ltd. Java and all Java-based trademarks
# and logos are trademarks or registered trademarks of Oracle and/or its affiliates. HCL, the HCL logo,
# and Tivoli are registered trademarks of HCL Technologies in the United States, other countries, or both.
#######################################################################################################################
#
# changes all detected issue-type severities to major
#

# execfile("_defs.py")
from _defs import *

SeverityHigh = 3

from CLR.System.Windows.Forms import MessageBox


# def ChangeToMajorHandler(sender, e):
#     MessageBox.Show("stopped")

def ChangeToMajorHandler(sender, e):
    ChangeToMajor(sdata.AppTreeRoot)


def ChangeToMajor(root):
    itypes = root.GetIssueTypes()
    for t in itypes:
        t.Severity = SeverityHigh
    scan.SaveScanData("tmp.scan")


scan.ScanEnded += ChangeToMajorHandler
