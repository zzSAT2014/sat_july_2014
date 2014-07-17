#access to modules in the upper level, mainly dictionary from word bank
import sys
sys.path.append('/Users/Zhe/Desktop/sat_july_2014')

#access to current level
import os
subdir = os.path.dirname(__file__)
sys.path.append(subdir)

import re

from print_dict import print_dict
from sub_dic import sub_dict
from word_bank import dictionary
from data import data
from parser import txt_parser

def word_add(date):
	'''input <---date

	output ----> update function'''
	def inner(tup):
		'''change the inner tuple corresponding to each word
		input  <--  (numdates , [date1,date2...])	

		output -->   (numdates+1,  [date1, date2, date3, date4....])'''
		num, lis = tup
		lis.append(date)
		num = len(lis)
		return (num,lis)
	return inner


def appender(x):
	'''appending function with stuff to be appended as function constructor, x'''
	def inner(lis):
		'''input <--- lis

		output ---> lis.append(x)'''
		lis.append(x)
		return lis
	return inner






def index_2_word(lisNum):
	'''translate index to word
	set lisNum

	output ---> inner function
	'''

	def inner(coor):
		'''input <--- coordiantes

		output ---> word'''
		return dictionary.get_w((lisNum,coor))
	return inner

# l_trans=index_2_word('l5')
# print l_trans('D2')

class vocab_parser(txt_parser):
	def __init__(self,filename):
		'''custom designed vocab template processing toool'''
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
					l_trans = index_2_word(listNum)  #list-specific translator


					tested = map(l_trans,re.split(',',tested) ) #translate to word 	
					if wrong == 'None': wrong = []
					if len(wrong) >0: wrong = map(l_trans,re.split(',',wrong))	#translate to word
					correct = [a for a in tested if a not in wrong]#maybe i will add untested word later


					correctRate = len(correct)/float(len(tested))


					sub_dict(dic,[name,'vocab','date',date],func = appender((listNum,correctRate)),value=[]) #date specific : date:[(listNum,correctRate).....] appender
					#print dic
					sub_dict(dic,[name,'vocab','list',listNum],func = appender((date,correctRate)) ,value=[]) #list specific : lisNum:[(date,correctRate).....] appender
					#print dic

					for cate,identi,flag in [(wrong,'wrong',False),(correct,'correct',True)]:    #word specific: word: wrong : (numdates,[....]), correct : (numdates,[....]), mostRecent : (flag,date)
						for word in cate: #for word in each category
							#translate(word)
							sub_dict(dic,[name,'vocab','word',word,identi],func=word_add(date) ,value = (0,[]))
							sub_dict(dic,[name,'vocab','word',word,'mostRecent'],func =lambda x: (flag,date),value=()) #
		return inner

def test_basic_parser():
	
	# data_file = '/Users/Zhe/Desktop/sat_july_2014/data_2014.07.15/test'
	data_file = subdir + '/'+'empty'
	input= 'vocab_test'

	original = data(data_file)
	a = vocab_parser(subdir + '/'+input).parser()

	original.update(a,output = 'test_output')
	#a(empty)
	#print_dict(empty)

#test_basic_parser()
#test_vocab_parser()
