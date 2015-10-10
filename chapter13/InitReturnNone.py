#P346

class Phone(object):
	def __init__(self,pn,prefix = '027'):
		self.phonenum = pn
		self.prefix = '027'
		print 'initialized'
		return 1

p = Phone('32452345')
