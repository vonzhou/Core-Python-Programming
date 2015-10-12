#P192

def getAction(cmd):
	action = 'invalid choice...try again'
	if cmd in ('create', 'delete', 'update'):
		action = '%s item'  % cmd

	return action

print getAction('update')
print getAction('fck')
