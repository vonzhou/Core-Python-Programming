#P208

f = open('hello.txt', 'r')
longest = 0
allLines = [x.strip() for x in f.readlines()]
f.close() #...

for line in allLines:
	lineLen = len(line)
	if lineLen > longest:
		longest = lineLen

print 'Longest Line:',longest

