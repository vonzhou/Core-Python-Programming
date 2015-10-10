#P341

class Phone(object):
	def __init__(self,pn,prefix = '027'):
		self.phonenum = pn
		self.prefix = '027'

p = Phone('1234567')
print type(p)
print type(0)

print type(Phone)
print type(int)
