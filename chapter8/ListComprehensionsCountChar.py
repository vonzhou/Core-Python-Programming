#P206

f = open('hello.txt', 'r')

#count words
wordList =  [word for line in f for word in line.split()]
print len(wordList)


# count char s
f.seek(0)
wordLenList = [len(word) for line in f for word in line.split()]
charCount = sum(wordLenList)
print charCount

# optimize  P207
f.seek(0)
print sum(len(word) for line in f for word in line.split())

print '----------------------'

rows = [1, 2, 3, 7]
def cols():
	yield 56
	yield 2
	yield 1

x_product_pars = [(i,j) for i in rows for j in cols()]
for pair in x_product_pars:
	print pair

