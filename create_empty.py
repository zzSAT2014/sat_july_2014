import codecs
import os 

def open(filename,mode='a+'):
	'''convert to utf-16 mode, for universial compatibility
	'''

	# print 'hi'
	return codecs.open(filename,mode,'utf_8')

filename = 'empty'
#os.remove('empty')
f = open(filename)
f.write('{}'.encode('utf_8'))
f.close()
f=open(filename,'r+')
print #f.read()
for line in f:
	print line
	a=eval(line)
a['b']='c'
print a

# f = codecs.open('ttttt', encoding='utf_8', mode='a+')
# f.write(u'\u4500 blah blah blah\n')
# a= 'a'.encode('utf_8')
# print a
# f.close()