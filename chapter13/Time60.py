

class Time60(object):
	def __init__(self, h, m):
			self.hour = h
			self.minute = m
	def __str__(self):
		return "%d:%d" % (self.hour, self.minute)

	def __add__(self, other):
		return self.__class__(self.hour+other.hour, self.minute+other.minute)

	__repr__ = __str__

	def __iadd__(self,other):
		self.hour += other.hour
		self.minute += other.minute
		return self



mon = Time60(2, 30)
tu = Time60(12, 40)

print mon,tu
print mon+tu
mon += tu
print mon
