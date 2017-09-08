import os, time, shutil, datetime, csv, logging #, pypyodbc

#Logging basics
logging.basicConfig(filename="DirectoryListener.log", level=logging.DEBUG)


##Test SQL connection
##ConnectionString = 'Driver={SQL Server Native Client 11.0};Server=<EE-L-7001309\MARTINTESTER>;Database=<Testers>;Uid=<DirectoryListener>;Pwd=<DIR>;'
##DbConnection = pypyodbc.connect(ConnectionString)
##DbQuery = 'SELECT [ID],[SerialNumber],[Line] FROM [Testers].[dbo].[SAP_Products]'
##ConnectionCursor = DbConnection.cursor()
##ConnectionCursor.execute(DbQuery)
##ConnectionCursor.close()
##DbConnection.close()

#Import listdir module
from os import listdir

#Source path
SourcePath = "C:\Python\\"

#Current year for DestPath
CurrentYear= datetime.datetime.now().strftime("%Y")
DestPath = "C:\Python\Archive\\" + CurrentYear + "\\"   #This will be later moved to #Move file to archive


#Dictionary from last check
DirMemory = dict ([(DirObject, None) for DirObject in os.listdir (SourcePath)])
while 1:
    time.sleep (10) #Check every 10 seconds
    After = dict ([(DirObject, None) for DirObject in os.listdir (SourcePath) if DirObject.endswith('.sap')] )
    Added = [DirObject for DirObject in After if not DirObject in DirMemory]
    DirMemory = After

    for SapFile in Added:

        #Read the file and assign to variables
        SerialNumber = []   #Get SerialNumber from .sap file
        SapFileSource = os.path.join(SourcePath, SapFile)
        SapFileRead = open(SapFileSource, 'r')
        SapFileContent = csv.reader(SapFileRead, delimiter ='\t')   #SapFileRead.read()

        #Append SerialNumber from .sap file
        for row in SapFileContent:
            SerialNumber.append(row[0])
        ContentLength = len(row)
        SapFileRead.close()
        print (ContentLength, SerialNumber)
        #Move file to archive
        shutil.move(os.path.join(SourcePath, SapFile), DestPath)
        logging.debug(SapFile + " was moved to " + DestPath)

#Print path file list
#for Object in DirObject:
#    print (Object)
