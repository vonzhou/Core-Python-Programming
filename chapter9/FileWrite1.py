# P218
import os

filename = raw_input("Enter file name:")
fobj = open(filename, 'w')
while True:
	aLine = raw_input("Enter a line ('.' to quit):")
	if aLine != '.':
		fobj.write("%s%s" %(aLine, os.linesep))
	else:
		break

fobj.close()


