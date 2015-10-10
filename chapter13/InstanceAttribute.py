#P346

class C(object):
	pass

c = C()
print dir(c)
print c.__dict__
print c.__class__


c.foo = 'foo'
c.bar = 'vonzhou'

print dir(c)
print c.__dict__

