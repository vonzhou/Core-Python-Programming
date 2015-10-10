#P353

from Name import Name 
from Phone import Phone

class NewAddrBookEntry(object):
	def __init__(self, nm, pn):
		self.name = Name(nm)
		self.phone = Phone(pn)
		print "Create a book entry for ",self.name.toString()


be = NewAddrBookEntry("vonzhou", "4352345235")
