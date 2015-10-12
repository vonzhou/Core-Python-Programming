#P366

class C(object):
	pass

c = C()
c.foo = 100
c.bar = 'vonzhou'

print c.__dict__
print vars(c)
print vars()

