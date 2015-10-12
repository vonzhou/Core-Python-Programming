#P192

def getAction(cmd):
	action = 'invalid choice...try again'
	if(cmd == 'create'):
		action = 'create item'
	elif(cmd == 'delete'):
		action = 'delete item'
	elif(cmd == 'update'):
		action = 'update'

	return action

print getAction('update')
print getAction('fck')
