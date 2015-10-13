#P208

f = open('hello.txt', 'r')
longest = 0
allLines = f.readlines()
f.close() #...

for line in allLines:
	lineLen = len(line.strip())
	if lineLen > longest:
		longest = lineLen

print 'Longest Line:',longest

