
# ''' P342'''
class P(object):
	def __del__(self):
		print 'parent deleted'

class C(P):
	def __init__(self):
		print 'initialized'
	def __del__(self):
		P.__del__(self)
		print 'deleted'

c1 = C()
print '-------'
c2 = c1
c3 = c1
print id(c1)
print id(c2)
print id(c3)

print '-------------'
del c1 
del c2
del c3

raw_input()
