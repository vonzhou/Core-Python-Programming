
class P1:
	def foo(self):
		print "calling P1-foo()...."

class P2:
	def foo(self):
		print "calling P2-foo()..."
	def bar(self):
		print "calling P2-bar()..."

class C1(P1,P2):
	pass

class C2(P1,P2):
	def bar(self):
		print "calling C2-bar()...."

class GC(C1,C2):
	pass


g1 = GC()
g1.foo()
print "-----------------"
g1.bar()
