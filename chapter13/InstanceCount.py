
''' P343'''

class InsCnt(object):
	count = 0    # count is a Class attribute
	def __init__(self):
		InsCnt.count += 1
	def __del__(self):
		InsCnt.count -= 1
	def howMany(self):
		return InsCnt.count

c1 = InsCnt()
print c1.howMany()

c2 = c1 
print c2.howMany()


c3 = InsCnt()
print c3.howMany()

del c1 
del c2
print c3.howMany()
del c3
print c3.howMany()

raw_input()
raw_input()
