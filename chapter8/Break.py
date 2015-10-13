#P199

def maxDivisor(num):
	count = num / 2
	while count > 0:
		if num % count == 0:
			print count, 'is the largest factor of', num
			break
		count -= 1

num = 96
maxDivisor(num)
