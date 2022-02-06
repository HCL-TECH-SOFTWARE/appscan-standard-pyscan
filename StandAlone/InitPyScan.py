import os
import sys
import CLR


# If the script is working from within a directory with AppScan - use the current directory to load
# the AppScanSDK.dll. Otherwise - use AppScan's installation directory
def GetWorkDir():
    if len(filter(lambda x: x == "AppScan.exe", os.listdir('.'))) == 1:
        return '.'
    else:
        return GetAppScanDir()


def GetAppScanDir():
    import _winreg
    k = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, "Software\\IBM\\AppScan Standard")
    return _winreg.QueryValueEx(k, "AppScanDir")[0]


# Perform a series of imports in order to make AppScan available
def InitClrConnection():
    sys.path.append(GetWorkDir())
    import CLR
    try:
        from CLR.AppScanSDK import AppScan
    except:
        from CLR import AppScan
        try:
            from CLR.GuiLayerSDK import AppScan
        except:
            try:
                from CLR.AppScan import AppScan
            except:
                from CLR.AppScan.Gui import MainForm


InitClrConnection()

from CLR import AppScan

appScan = AppScan.AppScanFactory.CreateInstance()
