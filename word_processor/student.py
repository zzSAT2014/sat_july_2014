#access from super level
import sys
sys.path.append('/Users/Zhe/Desktop/sat_july_2014')

from pprint import pprint
#pprint(sys.path)

import re
import os
subdir = os.path.dirname(__file__)
sys.path.append(subdir)

#access collector from upper level
from collector import mydata
from collector import print_dict
from weighted_random import weighted_choice


#sub_dict(dic,lis,func=lambda x:x,value=None,copy=None)
#i have these important information

data = mydata
#print data
def open(filename,mode='a+'):
	'''convert to utf-16 mode, for universial compatibility
	'''
	#print 'hi'
	return codecs.open(filename,mode,'UTF-8')



class student(object):
	'''get all inforamtion about an individual student
	{zhe:straight, li:gay} --> zhe --> {straight} '''
	def __init__(self,name,data_object):
		if name in data.info: self.info = data_object.get_student(name)
		else: self.info={} 
		self.name = name
	def __str__(self):
		print_dict(self.info)
		return 'end'

def test_student():
	a = student('LiZhijian',mydata)
	print a
#test_student()