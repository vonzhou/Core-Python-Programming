#P362

print issubclass(dict,object)
print issubclass(dict, dict)

d = {"name":"vonzhou", "age":12}
print isinstance(d,dict)

print '-----------------'

class C1(object):
	pass

class C2(object):
	pass

class C3(object):
	pass

c1 = C1()
c2 = C2()
print isinstance(c1, C1)
print isinstance(c1, C2)
print isinstance(c1, (C1, C2, C3))
#print isinstance(c1, c2)

print '---------------------'
print isinstance(4, int)
print isinstance(4, str)



