#P354

class Parent(object):
	'Parent Class Doc'
	def parentMethod(self):
		print 'calling parent method'

class Child(Parent):
	def childMethod(self):
		print 'calling child method'

p = Parent()
p.parentMethod()

c = Child()
c.parentMethod()
c.childMethod()
print c.__doc__
