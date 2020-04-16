#! python3

# Write a program that walks through a folder tree and searches for files with a certain file extension (.pdf / .jpg)
# Copy these files from whatever location they are in to a new folder

import os, shutil

def selectiveCopy(folder, extensions, destFolder):
    folder = os.path.abspath(folder)
    if os.path.exists(destFolder) != True:
        os.mkdir(destFolder)
    destFolder = os.path.abspath(destFolder)
    print('Looking in {} for files with extensions of {}'.format(folder, ' and '.join(extensions)))
    for foldername, subfolders, filenames in os.walk(folder):
        if foldername == destFolder:
            continue
        for filename in filenames:
            name, extension = os.path.splitext(filename)
            if extension in extensions:
                fileAbsPath = foldername + os.path.sep + filename
                print('Copying {} to {}'.format(fileAbsPath, destFolder))
                shutil.copy(fileAbsPath, destFolder)

extensions = ['.txt', '.py']
folder = (r'<yourpath>')
destFolder = (r'<yourpath>')
selectiveCopy(folder, extensions, destFolder)

