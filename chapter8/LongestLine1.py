#P208

f = open('hello.txt', 'r')
longest = 0
line = f.readline().strip()
while line:
	lineLen = len(line)
	if lineLen > longest:
		longest = lineLen
	line = f.readline().strip()

f.close()
print 'Longest Line:',longest

