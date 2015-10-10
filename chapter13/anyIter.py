

class AnyIter(object):
	def __init__(self,data, safe = False):
		self.iter = iter(data)
		self.safe = safe
	def __iter__(self):
		return self
	def next(self, howMany = 1):
		retval = []
		for item in range(howMany):
			try:
				retval.append(self.iter.next())
			except StopIteration:
				if self.safe:
					break
				else:
					raise
		return retval

a = AnyIter(range(10))
i = iter(a)
for j in range(1,5):
	print j,":", i.next(j)
				
print "--------------"	
#print i.next(11)	

a = AnyIter(range(10), True)
i = iter(a)
print i.next(12)


