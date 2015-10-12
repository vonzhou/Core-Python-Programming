#P193

def min1(x,y):
	if x<y:
		return x
	else:
		return y

def min2(x, y):
	return (x < y and [x] or [y])[0]

def min3(x, y):
	return (x if x < y else y)


x = -3
y = 0
print min1(x, y)
print min2(x, y)
print min3(x, y)
