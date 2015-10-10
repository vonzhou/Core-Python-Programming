#P359

class RoundFloat(float):
	def __new__(cls,val):
		#return float.__new__(cls, round(val,2))
		return super(RoundFloat, cls).__new__(cls, round(val,2))


print RoundFloat(3.14159)
print RoundFloat(3.55666)
