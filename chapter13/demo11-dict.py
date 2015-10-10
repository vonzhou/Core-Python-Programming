
class SortedKeyDict(dict):
	def keys(self):
		return sorted(super(SortedKeyDict,self).keys())


d = dict((("vonzhou",23),("fang",20),("luyna", 22),))
sd = SortedKeyDict((("vonzhou",23),("fang",20),("luyna", 22),))
print d.keys()
print sd.keys()

print '-------------'
print 'By iterator:'.ljust(12),[key for key in sd]
print 'By keys:'.ljust(12), sd.keys()
