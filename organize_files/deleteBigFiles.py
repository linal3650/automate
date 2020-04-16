#! python3

# Write a program that walks through a folder tree and searches for exceptionally large files or folders
# File size of more than 100 MB, print these files with their absolute path to the screen

import os, send2trash

maxSize = 100
# Convert bytes to megabytes
def mb(size):
    return size / (3036)

path = (r'<your path>')

print("Files with a size bigger than " + str(maxSize) + " MB:")

for foldername, subfolders, filenames in os.walk(path):
    for filename in filenames:
        size = os.path.getsize(os.path.join(foldername, filename)) # returns size in bytes, bytes->kb->mb->gb (1024)
        size = mb(size)
        if size >= maxSize:
            print(os.path.join(foldername, filename))
            #send2trash.send2trash(os.path.join(foldername, filename)) # Uncomment after confirming

