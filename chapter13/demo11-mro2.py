
class B(object):
	pass

class C(object):
	def __init__(self):
		print "default constructor"

class D(B,C):
	pass

d = D()
