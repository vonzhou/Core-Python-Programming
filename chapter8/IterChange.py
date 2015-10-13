#P204

myDict = {'a':12, 'b':234, 'c':3}

for eachKey in myDict:
	print eachKey, myDict[eachKey]
	myDict[eachKey] = 111

for eachKey in myDict:
	print eachKey, myDict[eachKey]
	del myDict[eachKey]

