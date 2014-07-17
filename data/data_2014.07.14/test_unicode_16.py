import codecs
import string
import re
def test_code():
	with codecs.open('b.txt','r+','utf_8') as f:
		save = ''
		a={u'QianyiShi': {u'Barron3500': u'2', u'Taken': u'24', u'Score': u'0', u'Location': u'Guangzhou', u'CR': u'1', u'Test': u'570', u'Email': u'shiqianyicindy@163.com', u'DirectHits': u'1', u'TOEFLL': u'0', u'Wechat': u'13422347646', u'\u59d3\u540d': u'\u77f3\u5029\u6021', u'Date': u'730', u'TOEFLR': u'0', u'TOEFLS': u'1', u'TOEFLW': u'0', u'School': u'1', u'MA': u'99', u'ES': u'26', u'Tel': u'13422347646', u'Barron800': u'4', u'Grade': u'11', u'High': u'3', u'TOEFL\uff1f': u'22', u'SAT': u'1940', u'Total': u'1', u'WR': u'27'}}
		#print f
		#print f.readlines()
		# for line in f:
		# 	print repr(line)
		# 	print repr(line.split())
		# 	save = line
		

		output = codecs.open('out','a+','utf_8')
		# output.write()

		stri = str(a)
		b=re.sub("u'","'",stri)
		output.write(b.encode('utf_8'))
		
test_code()