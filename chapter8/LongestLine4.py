#P208

f = open('hello.txt', 'r')
allLines = [len(x.strip()) for x in f]
f.close() 

print 'Longest Line:',max(allLines)

