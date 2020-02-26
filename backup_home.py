#! python3

import zipfile, os

def backupToZip(folder):
    folder=os.path.abspath(folder)
    number=1
    while True:
        zipFilename=os.path.basename(folder)+''+str(number)+'.zip'
        if not os.path.exists(zipFilename):
            break
        number=number+1
#add zip-file
    print('file is created with name %s...:' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')
    print('Done')

backupToZip('/tmp')
