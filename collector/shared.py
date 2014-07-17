import codecs


def open(filename,mode='a+'):
	'''convert to utf-16 mode, for universial compatibility
	'''
	#print 'hi'
	return codecs.open(filename,mode,'UTF-8')

