#P365

class MyClass(object):
	def __init__(self):
		self.foo = 100 #default instance attribute

a = MyClass()
print hasattr(a, 'foo')
print getattr(a, 'foo')

#print getattr(a, 'bar')  #AttributeError
print getattr(a, 'bar', 'oops!')
print setattr(a, 'bar', 'my bar attr')
print dir(a)

print getattr(a, 'bar')
delattr(a, 'foo')
print dir(a)
print hasattr(a, 'foo')
print dir()



