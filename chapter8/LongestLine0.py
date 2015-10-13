#P208

f = open('hello.txt', 'r')
longest = 0
while True:
	line = f.readline()
	#print '#',line,
	if not line:
		#print line == ''
		break # EOF  NB. line == ''
	lineLen = len(line.strip())
	if lineLen > longest:
		longest = lineLen

f.close()
print 'Longest Line:',longest


