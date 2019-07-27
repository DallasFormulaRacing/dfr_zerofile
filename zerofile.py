'''
When passed any number of directories, zerofile.py will check iterate
all the files within the subdirectories. Empty .txt files are deleted;
otherwise, the files are parsed and the values of two parameters, RPM
and coolant temp, are checked to see the instance of the log file. If
the values indicate an instance of system power being on (RPM = 0 and
an unchanging coolant temp), then the file is deleted.
'''
import sys
import os

def main():
	dirs = sys.argv

	#Iterating through the directories passed as arguments
	for x in range(1, len(dirs)):
		for subdir, dir, files in os.walk(dirs[x]):
			for file in files:
				filepath = subdir + os.sep + file
				statinfo = os.stat(filepath)

				#Initial check for.txt file format
				if (filepath.endswith(".txt")):
					if (statinfo.st_size != 0):
						#Checking and deleting files that have 0 RPM
						#and an unchanging coolant temp
						RPM_flag = True
						RPM = -1
						coolant_temp = -1
						coolant_flag = True
						log = open(filepath, 'r')

						for line in log:
							message = line.split()
							if (len(message) > 1):
								message = message[1].rstrip()
								identifier = message[0:4]

								#Identifier for PE1 message
								if (identifier == "#001"):
									RPM = message[4:8]
									RPM_value = int(RPM[0:2], 16)+int(RPM[2:4], 16)*256
									if (RPM_value != 0):
										RPM_flag = False
										break
								#Identifier for PE6 message
								elif (identifier == "#006"):
									#print(message)
									coolant_temp = message[12:16]
									coolant_temp = int(coolant_temp[0:2], 16)+int(coolant_temp[2:4], 16)*256
									#print(coolant)
									#print(coolant_value)
						log.close()
						if (RPM_flag and coolant_flag and RPM != -1):
							os.remove(filepath)
						#print("###########################")
					else:
						#Removing empty .txt files
						os.remove(filepath)

main()
