import os, time, shutil, datetime

#Import listdir module
from os import listdir

#Source path
SourcePath = "C:\Python\\"

#Current year for DestPath
CurrentYear= datetime.datetime.now().strftime("%Y")
DestPath = "C:\Python\Archive\\" + CurrentYear + "\\"


#Dictionary from last check
DirMemory = dict ([(DirObject, None) for DirObject in os.listdir (SourcePath)])
while 1:
    time.sleep (10) #Check every 10 seconds
    After = dict ([(DirObject, None) for DirObject in os.listdir (SourcePath) if DirObject.endswith('.sap')] )
    Added = [DirObject for DirObject in After if not DirObject in DirMemory]
    DirMemory = After

    #Move file to archive
    for ToBeMoved in Added:
        shutil.move(os.path.join(SourcePath, ToBeMoved), DestPath)
        print (ToBeMoved + " was moved to " + DestPath)

#Print path file list
#for Object in DirObject:
#    print (Object)
