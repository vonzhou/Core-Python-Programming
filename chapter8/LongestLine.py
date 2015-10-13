#P208

f = open('hello.txt', 'r')
longest = 0
while True:
	lineLen = len(f.readline().strip())
	if not lineLen:
		break
	if lineLen > longest:
		longest = lineLen

f.close()
print 'Longest Line:',longest

