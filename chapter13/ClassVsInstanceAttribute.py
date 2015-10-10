#P348

class C(object):
	version = 1.2

c = C()
print C.version
print c.version

C.version += 0.1

print C.version
print c.version

class Foo(object):
	x = 1.5

foo = Foo()
print foo.x
foo.x = 1.7
print foo.x
print Foo.x

del foo.x
print foo.x

foo.x += 0.2
print foo.x 
print Foo.x

print 'volatile class attribute'
class Bar(object):
	x = {2003:'poe'}

bar = Bar()
print bar.x
bar.x[2004] = 'valid path'
print bar.x
print Bar.x   #changed!!

del bar.x





