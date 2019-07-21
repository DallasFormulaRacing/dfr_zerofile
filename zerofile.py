'''
When passed any number of directories, zerofile.py deletes all
the files of size 0 within those directories and subdirectories.
'''
import sys
import os

dirs = sys.argv

#Iterating through the directories passed as arguments
for x in range(1, len(dirs)):
	for subdir, dir, files in os.walk(dirs[x]):
		for file in files:
			filepath = subdir + os.sep + file

			statinfo = os.stat(filepath)
			#If a given file has a size 0, then remove that file
			if (statinfo.st_size == 0):
				os.remove(filepath)
