#access to modules in the upper level, mainly dictionary from word bank
import sys


#access to current level
import os
subdir = os.path.dirname(__file__)
sys.path.append(subdir)
sys.path.append(os.path.abspath(os.path.join(subdir, os.pardir)))


import re

from print_dict import print_dict
from sub_dic import sub_dict

from data import data
from parser import txt_parser

from vocab_parser import *





def lindex(lisNum):
	'''translate index to word
	set lisNum

	output ---> inner function
	'''

	def inner(coor):
		'''input <--- coordiantes

		output ---> word'''
		return (lisNum ,coor)
	return inner

# l_trans=index_2_word('l5')
# print l_trans('D2')

class CRmock_parser(txt_parser):
	def __init__(self,filename):
		'''custom designed vocab template processing toool'''
		print '\t CRmock_parser file: %s' %filename
		self.file = open(filename,'r')
		self.temp = {}
		self.info = []#(flag(wheter it is append),directory,result)

	def parser(self):
		def inner(dic):
			for index,line in enumerate(self.file):
				if index == 0: date=line.split()[1] #get dates
				elif index == 1: continue
				else:
					print line 
					name,listNum,tested,wrong = line.split()
					l_trans = lindex(listNum)  #list-specific translator

					basic_wrong = wrong.split(',')

					tested = map(l_trans,re.split(',',tested) ) #translate to real index
					if wrong == 'None': wrong = []
					if len(wrong) >0: wrong = map(l_trans,re.split(',',wrong))	#translate to real_index
					correct = [a for a in tested if a not in wrong]#maybe i will add untested word later


					correctRate = len(correct)/float(len(tested))


					sub_dict(dic,[name,'CRmock','date',date],func = appender((listNum,correctRate,basic_wrong)),value=[]) #date specific : date:[(listNum,correctRate).....] appender
					#print dic
					sub_dict(dic,[name,'CRmock','list',listNum],func = appender((date,correctRate,basic_wrong)) ,value=[]) #list specific : lisNum:[(date,correctRate).....] appender
					#print dic

					for cate,identi,flag in [(wrong,'wrong',False),(correct,'correct',True)]:    #word specific: word: wrong : (numdates,[....]), correct : (numdates,[....]), mostRecent : (flag,date)
						for word in cate: #for word in each category
							#translate(word)
							sub_dict(dic,[name,'CRmock','word',word,identi],func=word_add(date) ,value = (0,[]))
							#sub_dict(dic,[name,'vocab','word',word,'mostRecent'],func =lambda x: (flag,date),value=()) #
		return inner

def test_mock_parser():
	
	# data_file = '/Users/Zhe/Desktop/sat_july_2014/data_2014.07.15/test'
	data_file = subdir + '/'+'empty'
	input= 'mock_test'

	original = data(data_file)
	a = CRmock_parser(subdir + '/'+input).parser()

	original.update(a, output = subdir + '/'+'test_output')
	print original
	#print_dict(empty)

#test_mock_parser()