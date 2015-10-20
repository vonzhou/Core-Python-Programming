# P223
import os

for tmpdir in ('/tmp', 'F:\\'):
	if os.path.isdir(tmpdir):
		break
	else:
		print 'no temp dir available'
		tmpdir = ''

if tmpdir:
	os.chdir(tmpdir)
	cwd = os.getcwd()
	print '*** current temp work dir:', cwd
	print '*** creating example directory...'
	os.mkdir('example')
	os.chdir('example')
	cwd = os.getcwd()
	print '*** new work dir:', cwd

	print '*** original dir listing:'
	print os.listdir(cwd)

	print '*** creating test file...'
	fobj = open('test', 'w')
	fobj.write('foo\n')
	fobj.write('bar\n')
	fobj.close()
	print '*** updated dir listing:'
	print os.listdir(cwd)

	print '*** rename test to filetest.txt'
	os.rename('test', 'filetest.txt')
	print '*** updated dir listing:'
	print os.listdir(cwd)

	path = os.path.join(cwd, os.listdir(cwd)[0])
	print '*** full file path name:', path

	print '*** (pathname, basename) :', os.path.split(path)
	print '*** (filename, extention) :', os.path.splitext(os.path.basename(path))

	print '*** displaying file content:'
	fobj = open(path)
	for eachLine in fobj:
		print eachLine,
	fobj.close()

	print '*** delete test file'
	os.remove(path)
	print '*** updated dir listing:'
	print os.listdir(cwd)

	os.chdir(os.pardir)
	print '*** delete test dir'
	os.rmdir('example')
	print '*** DONE'










