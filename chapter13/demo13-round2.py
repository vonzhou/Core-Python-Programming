

class RoundFloatMannual(object):#(float):
	def __init__(self,val):
		assert isinstance(val,float),"Value must be float!"
		self.value = round(val,2)
	def __str__(self):
		#return str(self.value)
		return "%.2f" % (self.value)
	__repr__ = __str__

#r = RoundFloatMannual(44)
r = RoundFloatMannual(5.5964)
print r

print str(r)*2



