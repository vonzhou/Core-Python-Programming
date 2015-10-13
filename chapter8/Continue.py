#P200

def checkPwd():
	valid = False
	count = 3
	passwordList = ('123456', 'vonzhou')
	while count > 0:
		input = raw_input('Enter password:')
		for each in passwordList:
			if input == each:
				valid = True
				break

		if not valid:
			print 'invalid input password'
			count -= 1
			continue
		else:
			print 'Good input'
			break

checkPwd()



