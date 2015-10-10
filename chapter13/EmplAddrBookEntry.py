class AddrBookEntry(object):
	'address book entry class'
	def __init__(self, nm, ph):
		self.name = nm
		self.phone = ph
		print 'Created instance for: ', self.name

	def updatePhone(self, newph):
		self.phone = newph
		print 'Updated phone# for:', self.name

class EmplAddrBookEntry(AddrBookEntry):
	'employee address book entry class'
	def __init__(self, nm, ph, id, em):
		AddrBookEntry.__init__(self, nm, ph)
		self.empid = id
		self.email = em

	def updateEmail(self, newem):
		self.email = newem
		print 'Updated email for:', self.name

john = EmplAddrBookEntry('John Doe', '2342134', '1', 'abcdefg@qq.com')

print john
print john.name
print john.phone
print john.email
print 'Class Doc:', EmplAddrBookEntry.__doc__

john.updatePhone('66666666')
john.updateEmail('123456@gmail.com')

print john.email




