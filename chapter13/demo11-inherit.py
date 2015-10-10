
class P(object):
	'parent P class'
	def __init__(self):
		print "creat an instance of", self.__class__.__name__

class C(P):
	pass


p = P()
print p.__class__
print P.__base__
print P.__doc__

print '-------------------'
c = C()
print c.__class__
print C.__base__
print C.__doc__
