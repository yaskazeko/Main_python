#! python3

import os
import zipfile


def backup_to_zip(folder):
    print("test")
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zip_filename = os.path.basename(folder) + '' + str(number) + '.zip'
        if not os.path.exists(zip_filename):
            break
        number = number + 1
    # add zip-file
    print('file is created with name %s...:' % zip_filename)
    backup_zip = zipfile.ZipFile(zip_filename, 'w')
    #    print('Done')
    # walk
    for foldername, subfolders, filenames in os.walk(folder):
        print('adding files from folder %s...' % folder)
        backup_zip.write(folder)
        for filename in filenames:
            if filename.startswith(os.path.basename(folder) + '_') and filename.endswith('.zip'):
                continue
            backup_zip.write(os.path.join(folder, filename))
    backup_zip.close()
    print('Done')


backup_to_zip('~/updater/')
