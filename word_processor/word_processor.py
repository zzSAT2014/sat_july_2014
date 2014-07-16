#access from super level
import sys
sys.path.append('/Users/Zhe/Desktop/sat_july_2014')

from pprint import pprint
pprint(sys.path)

import re
import os
subdir = os.path.dirname(__file__)
sys.path.append(subdir)

from word_bank import dictionary
from datetime import date

#access collector from upper level
from collector import mydata
from weighted_random import weighted_choice


#sub_dict(dic,lis,func=lambda x:x,value=None,copy=None)
#i have these important information

data = mydata

def open(filename,mode='a+'):
	'''convert to utf-16 mode, for universial compatibility
	'''
	#print 'hi'
	return codecs.open(filename,mode,'UTF-8')



class student(object):
	'''get all inforamtion about an individual student'''
	def __init__(self,name):
		if name in data.info: self.info = data.get_student(name)
		else: self.info={} 
		self.name = name
	def __str__(self):
		print_dict(self.info)
		return 'end'

class student_vocab(student):
	def __init__(self,name):
		student.__init__(self,name)
		if 'vocab' not in self.info:
			sub_dict(self.info,['vocab','list'],value=())
			sub_dict(self.info,['vocab','word'],value={})
		self.info = self.info['vocab']




get_coor = lambda tu: tu[1]

#add datetime module later for evaluation
class student_vocab_list(student_vocab):

	def __init__(self,name,lis_num):
		'''return student_specific, list_specific information and probabily process it'''
		student_vocab.__init__(self,name)


		self.wordsInDict = dictionary.get_l(lis_num) #all words inside a list
		testedlists = self.info['list'] #to see which one has been tested

		if lis_num not in testedlists: 
			self.basic = {}   #---> [(date,correctness)]
		else: self.basic = self.info['list'][lis_num]


		self.lis_num = lis_num
		all_tested_words = self.info['word'] #all words that have their data recorded

		
		self.list = []
		self.allwords = {}
		for word in self.wordsInDict:
			if word in all_tested_words:
				self.allwords[word] = all_tested_words[word]
				self.date = all_tested_words[word]['mostRecent']
		for word in self.wordsInDict:
			if word not in all_tested_words: self.allwords[word] = None
		#self.words[word] = None           
				#add the last revised time of when needed
		#get list
		for word in self.wordsInDict:
			self.list.append((weight_word(self.allwords[word]),word))

	trans = lambda self,word: dictionary.get_i(word,identifier = self.lis_num[0])

	def generate_list(self , num = 10):   
		#smaller num used to for testing, will change to larger value later
		#print self.list

		output = map(self.trans,weighted_choice(self.list,num = num))
		coordinates = map(get_coor,output)
		return (self.name ,self.lis_num, coordinates)





	# def generate(self,func):
	# 	'''a list '''
# gpNamel = ['zhe','chongzhang','zhouhan']
# lis_nums =['l1','l2','l3']
def generate_for_lis_groups(gpNamel,lis_nums):
	'''	input: gp --> a list containing all the names inside a group
				lis_num --> a list containing all numbers to be test_student

		output: list containing all information to be printed
	'''
	output = []
	for name in gpNamel:
		for lis_num in lis_nums:
			a = student_vocab_list(name,lis_num)
			output.append(a.generate_list())
	return output


class vocabulary_tests_data (object):
	"""
	input:data:[(name, listnum, vocab_test), (), () ]

	date will be supplied as an additional parameter

	output: generate txt file, same as vo_input_temp.txt

	"""
	def __init__(self,data,date):
		
		self.data = data
		self.date = date

	def process_line(self,atom):
		name, lis_num, words = atom
		return name + ' '*(20-len(name)) + lis_num + '\t'*4 + ','.join(words)

	def output(self,filename):
		a = open(filename,'a+')
		a.write('date '+self.date)
		a.write('\n')
		a.write('name' +'\t'*4+ 'listnum' + '\t'*4+'vocab,test' +'\t'*12+ 'vocab,false')
		a.write('\n')
		for atom in self.data:
			print atom#iterable
			a.write(vocabulary_tests_data.process_line(self,atom)+'\n')
		a.close()
#************************************************************
#use this to generate information
#input information
# name_gs =['sb1','sb2']
# groups = [['QianyiShi','HuijunLi'],['QianyiShi','HuijunLi']]
# lisnum_gs = [['Dl1', 'Bl2' , 'Dl3'],['Bl4', 'Bl5']]
name_gs =['sb','notsb1','notsb2']
groups = [['ZhangJianxin', 'GuoZiwei', 'ZhouMingrui', 'ChenYanghui', 'GaoYueMing', 'HuKangrui', 'LiuHuijun', 'ZhangShenghong'],
			['LiZhijian', 'ZhangXiaoying', 'ShiQianyi', 'ZhuoJiaming', 'ChenAnran', 'LiRuxian'],
			['GaoYichen', 'HuangYiheng', 'LiXingrong', 'WuShiqi', 'Mengruolin', 'XieChen']]
lisnum_gs = [['Dl5','Dl6','Dl8','Dl9'],['Dl5','Dl6','Dl8','Dl9'],['Dl5','Dl6','Dl8','Dl9']]

em = date.today()
date = '%s.%s.%s'%(em.year,em.month,em.day)

def generate_list_specific(name_gs,groups,lisnum_gs,date):
	'''generate all txt files need for testing, with name in name_gs+date  as filename'''
	print date
	for identifier, group, lisnums in zip(name_gs,groups,lisnum_gs):
		data = generate_for_lis_groups(group,lisnums)
		print data
		a = vocabulary_tests_data(data,date)
		a.output(identifier+date)



generate_list_specific(name_gs,groups,lisnum_gs,date)


def test_student():
	name='zhe'
	a = student_vocab_list(name,'l1')
	#print print_dict(a.words)
	#print a.generate_list()
	gpNamel = ['QianyiShi','HuijunLi']
	lis_nums =['Bl1','Bl2','Bl3']
	print generate_for_lis_groups(gpNamel,lis_nums)
#test_student()


