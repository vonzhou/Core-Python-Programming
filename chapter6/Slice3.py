#105

s = 'abcde'
i = -1
seq = [None]
seq.extend(range(-1, -len(s), -1))
for i in seq:
	print s[:i]

