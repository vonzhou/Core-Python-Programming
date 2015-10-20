# P218
import os

f = open('hello.txt', 'w+')
print f.tell()

f.write('test line 1\n')
print f.tell()

f.write('test line 2\n')
print f.tell()

f.seek(-13, 1)
f.tell()

print f.readline(),'#',

f.seek(0, 0)
print f.tell()
print f.readline()

print f.tell()


f.close()


