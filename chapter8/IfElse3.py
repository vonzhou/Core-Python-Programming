#P192

def getAction(cmd):
	msgs = {'create':'create item', 'delete item':'you delete item', 'update':'update item'}
	default = 'invalid choice...try again'
	action = msgs.get(cmd, default)

	return action

print getAction('update')
print getAction('fck')
