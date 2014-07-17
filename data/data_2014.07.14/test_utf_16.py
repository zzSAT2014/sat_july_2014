import codecs
f=codecs.open('b.txt','r','utf-8')
for line in f:
	print repr(line)