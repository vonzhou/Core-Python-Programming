#P208

f = open('hello.txt', 'r')
longest = max(len(x.strip()) for x in f)
f.close() 

print 'Longest Line:',longest

