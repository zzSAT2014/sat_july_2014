#access to modules in the upper level, mainly dictionary from word bank
import sys
sys.path.append('/Users/Zhe/Desktop/sat_july_2014')

#access to current level
import os
subdir = os.path.dirname(__file__)
sys.path.append(subdir)

import re

from shared import open
from print_dict import print_dict

class data(object):
	def __init__(self,filename,mode = 'r+'):
		'''opens up the file in r+ mode, unless otherwise specified, i.e use a+ to create file'''
		self.file = open(filename,mode = mode)
		self.name = filename
		# string=self.file.read().strip()
		string = ''
		for line in self.file:
			string = eval(line)
		#print 'hi'
		#print string
		self.info =  string
		self.file.close()

	def convert(self,data):
		'''basic parsing of utf_8 format for output'''
		string = str(data)
		out = re.sub("u'","'",string)
		print '\t data_convert:\tconverting information '
		return out.encode('utf_8')

	def update(self, func, output = 'newmaster'):
		'''modify the input and save it'''
		func(self.info)
		#print_dict(self.info)
		self.file = open(output,'a+')
		os.remove(output)
		self.file = open(output,'a+')
		#print self.info
		#print self.info
		self.file.write(self.convert(self.info))
		self.file.close()

	def get_student(self,name):
		'''return all information about the student'''

		#print_dict(self.info[name])
		if name in self.info: return self.info[name]
		else: return {}
	def __str__(self):
		print_dict(self.info)
		
		return 'end'


def test_data():
	#a= data('empty')
	
	input_file = '/Users/Zhe/Desktop/sat_july_2014/data_2014.07.15/test'
	a = data(input_file)
	print a

#test_data()