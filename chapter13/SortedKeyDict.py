#P359

class SortedKeyDict(dict):
	def keys(self):
		return sorted(super(SortedKeyDict, self).keys())


d = SortedKeyDict((('luyna', 100), ('jet', 34), ('vonzhou', 99)))
print 'By Iterator:'.ljust(12), [key for key in d]
print 'By keys():'.ljust(12), d.keys()


