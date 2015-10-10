# P336

class C(object):
	foo = 100

	def noActionMethod(self):
		pass


print C.foo

C.foo = C.foo + 1
print C.foo

c = C()
c.noActionMethod()


