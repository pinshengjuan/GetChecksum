import sys
import time
import pyperclip
import datetime
from pathlib import Path


def main():
	# print("Main start")

	if sys.getdefaultencoding() != 'utf-8':
		reload(sys)
		sys.setdefaultencoding('utf-8')

	FileName = sys.argv[1]
	ChecksumType = sys.argv[2]

	FileDir = Path.cwd() #get current working directory
	
	FileChecksum = GetFileChecksum(FileDir / FileName, ChecksumType)

	pyperclip.copy(FileChecksum) #copy checksum to clipboard

	return

def GetFileChecksum(File, type):
	f = open(File, "rb").read()
	
	if(type == "8"):
		numChecksum = sum(f) & 0xff # AND 0xff to get checksum-8
	elif(type == "16"):
		numChecksum = sum(f) & 0xffff # AND 0xffff to get checksum-16
	elif(type == "32"):
		numChecksum = sum(f) & 0xffffffff # AND 0xffffffff to get checksum-32

	strChecksum = "0x%X" %numChecksum #change to base-16

	return strChecksum

if __name__ == '__main__':
	main()