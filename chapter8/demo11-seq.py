

seq = (23, "vonzhou",True,34.99,)
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
	
		
