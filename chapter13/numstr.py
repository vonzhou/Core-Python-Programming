
class NumStr(object):
	def __init__(self,num=0, string=''):
		self.__num = num
		self.__string = string
	def __str__(self):
		return '[%d::%r]' % (self.__num, self.__string)
	__repr__ = __str__
	
	def __add__(self, other):
		if isinstance(other, NumStr):
			return self.__class__(self.__num + other.__num, self.__string + other.__string)
		else:
			raise TypeError, "The Add operation need NumStr type"
	
	def __mul__(self,n):
		if isinstance(n,int):
			return self.__class__(self.__num * n, self.__string * n)
		else:
			raise TypeError, "The Mul operation need a int type"

	def __nonzero__(self):
		return self.__num or len(self.__string)

	def __norm_cval(self,c):
		return cmp(c,0)

	def __cmp__(self, other):
		return self.__norm_cval(cmp(self.__num,other.__num)) + \
				self.__norm_cval(cmp(self.__string,other.__string))
	
a = NumStr(3, "foo")
b = NumStr(3, "goo")
c = NumStr(2, "foo")
d = NumStr()

print a
print a < b

print c * 2

print a + b

print "---------------"
print a._NumStr__num


		
