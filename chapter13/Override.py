#P357

class P(object):
	'parent P class'
	def __init__(self):
		print "creat an instance of", self.__class__.__name__
	def foo(self):
		print "I am P-foo().."


class C(P):
	def foo(self):
		print "I am C-foo().."


p = P()
p.foo()
print '-------------------'
c = C()
c.foo()
# call the parent's method using the child instance 
P.foo(c)
