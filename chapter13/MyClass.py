# P338 show what properties a class has

class MyClass(object):
	'My Class Definition'
	myVersion = '1.0'
	def showMyVersion(self):
		print MyClass.myVersion

print dir(MyClass)

print '------------------'

print MyClass.__dict__

print '------------------'

print MyClass.__name__
print MyClass.__doc__
print MyClass.__bases__
print MyClass.__class__

# type object
stype = type('what is your quest?')
print stype
print stype.__name__

print type(3.124)
print type(3.124).__name__




