
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
from sub_dic import sub_dict
from data import data

splitter= lambda string: re.split(',',string)
input_proce = lambda line: map(splitter,line.split()) #split the line by space, then split it by ',',return [[]...]


class txt_parser(object):
	'''return a parser function which mutates the info stored''' 
	def __init__(self,txtfile):
		'''parse a the input txt file into a list of tuples directory,value pair [([directory],[value]),(),()]
		directory a list of strings'''
		print 'basic info input filename%s\t'%txtfile
		self.file = open(txtfile,mode ='r')
		#for line in self.file: print line
		self.info = []
		for index,line in enumerate(self.file):
			if index == 0:
				#print line 
				#print 'hi'
				dirs = input_proce(line)
			else:
				line = input_proce(line)
				# print 'line 145%s' %line
				for i2,atom in enumerate(line):
					if i2 == 0: name = atom
					else:
						self.info.append((name+dirs[i2],atom))
		print 'line 41 input data inforamtion:\t%s'%self.info
	def parser(self):
		return None
	def __str__(self):
		print_dict(self.info)
		return 'end'


def test_txt_parser():

	input= 'input.txt'
	a=txt_parser(subdir + '/'+input)
	print a
#test_txt_parser()

class basic_parser(txt_parser):
	'''parse level 1 information,i.e only one element like name, age, sex etc
	substitute level 1 information function

	input --> txt file same as input.txt
	output --> modification function f
				[([a],c)..]---> f({a:b}) --> {a:c}
				 [([a,b],e)]---> F({a:{b,c:d}}) --> {a:{b:e,c:d}}'''
	def parser(self):
		def inner(dic):
			'''merely mutate value, does not return anything'''
			for directory,value in self.info:
				sub_dict(dic,directory,func = lambda x: value[0])
		return inner

def test_basic_parser():
	
	# data_file = '/Users/Zhe/Desktop/sat_july_2014/data_2014.07.15/test'
	data_file = subdir + '/'+'empty'
	input= 'input.txt'

	original = data(data_file)
	a = basic_parser(subdir + '/'+input).parser()

	original.update(a,output = 'test_output')
	#a(empty)
	#print_dict(empty)

#test_basic_parser()





