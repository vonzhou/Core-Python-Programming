
class B:
	pass

class C:
	def __init__(self):
		print "the default constructor"

class D(B,C):
	pass

d = D()
