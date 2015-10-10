class AddrBookEntry(object):
	'address book entry class'
	def __init__(self, nm, ph):
		self.name = nm
		self.phone = ph
		print 'Created instance for: ', self.name

	def updatePhone(self, newph):
		self.phone = newph
		print 'Updated phone# for:', self.name

john = AddrBookEntry('John Doe', '2342134')

print john
print john.name
print john.phone

john.updatePhone('66666666')



