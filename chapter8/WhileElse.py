#P201

def showMaxFactor(num):
	count = num / 2
	while count > 1:
		if num % count == 0:
			print 'largest fator of %d is %d' % (num, count)
			break
		count -= 1
	else:
		print num, 'is prime'

	#print '2 is prime'



for num in range(2, 12):
	showMaxFactor(num)


