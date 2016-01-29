#!/usr/bin/python3
import hashlib
import os
import sys

def getFileHashValue(fname):
	BLOCKSIZE = 65536	# good when we are dealing with big files.
	md5HashObj = hashlib.md5()
	with open(fname, 'rb') as binFileHandler:
		buf = binFileHandler.read(BLOCKSIZE)
		while len(buf) > 0:
			md5HashObj.update(buf)
			buf = binFileHandler.read(BLOCKSIZE)
	return md5HashObj.hexdigest()

# To either use the program from CMD or from a Python IDE
if len(sys.argv) < 2:
	os.chdir('./')
else:
	os.chdir(sys.argv[1])
	
dictFnameHashVal = {}
notUniq = 0

for f in os.listdir():
	if os.path.isfile(f):
		hashValue = getFileHashValue(f)
		if hashValue not in dictFnameHashVal.values():
			dictFnameHashVal[f] = hashValue
		else:
			notUniq += 1

# Write the results to file
with open('results.txt', 'w') as resFile:
	resFile.write("{0:50} {1}\n".format("File Name","Hash Value"))
	resFile.write("#" * 90 + "\n")
	# Check if the hash value is UNIQUE or not before writing
	for fName in dictFnameHashVal:
		if fName not in ['results.txt','hashcalc.py']:	# Don't want those in the results file
			resFile.write("{0:50} {1}\n".format(fName,dictFnameHashVal[fName]))	

#print(dictFnameHashVal)
print("The number of non-unique files is {0}".format(notUniq))

