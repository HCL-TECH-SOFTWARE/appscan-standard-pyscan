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
