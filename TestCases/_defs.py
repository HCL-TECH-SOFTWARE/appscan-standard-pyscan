a = appScan
scan = a.Scan
sdata = scan.ScanData
conf = sdata.Config

f = open("_config.txt")
lines1 = f.readlines()
f.close()
lines = [x.strip() for x in lines1]


conf.startingUrl = lines[0]

