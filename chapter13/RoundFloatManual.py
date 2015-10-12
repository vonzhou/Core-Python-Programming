#P370

class RoundFloatManual(object):
	def __init__(self, val):
		assert isinstance(val, float), 'Value arg must be a float'
		self.value = round(val, 2)

	def __str__(self):
		return '%.2f' % self.value
		#return str(self.value)

	__repr__ = __str__


#f = RoundFloatManual(42)
f = RoundFloatManual(4.2)
print f



