

class RoundFloatMannual(object):#(float):
	def __init__(self,val):
		assert isinstance(val,float),"Value must be float!"
		self.value = round(val,2)

#r = RoundFloatMannual(44)
r = RoundFloatMannual(44.34)
print r



