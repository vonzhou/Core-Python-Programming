#P111

import string

alphas = string.letters + '_'
nums = string.digits

print 'Welcome to the Identifier Checker v1.0'
print 'Testees must be at least 2 chars long.'
myInput = raw_input('Identifier to test?')

if len(myInput) > 1:
	if myInput[0] not in alphas:
		print 'invalid : first char must be alphabetic or underscore'
	else:
		alpnum = alphas + nums
		for otherChar in myInput[1:]:
			if otherChar not in alpnum:
				print 'invalid:remaining symbols must be alphanumeric'
				break
		else:
			print 'Ok as an Identifier'




