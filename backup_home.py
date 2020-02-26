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

    print('Done')

backupToZip('/tmp')
