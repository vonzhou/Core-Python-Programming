#P203

seq = (23, "vonzhou", True, 34.99,)


i = iter(seq)
print i.next()
print i.next()
print i.next()
print i.next()
print i.next()

for i in seq:
	print i

print "--------------"
fetch = iter(seq)
while True:
	try:
		i = fetch.next()
	except StopIteration:
		break
	print "iter:",i
	
		
