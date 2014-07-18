from datetime import date
import sys
sys.path.append('/Users/Zhe/Desktop/sat_july_2014')

from pprint import pprint
#pprint(sys.path)
from collector import mydata
import re
import os
subdir = os.path.dirname(__file__)
sys.path.append(subdir)

from student_vocab import student_vocab_list



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
name_gs =['sb','notsb1','notsb2']
groups = [['ZhangJianxin', 'GuoZiwei', 'ZhouMingrui', 'ChenYanghui', 'GaoYueMing', 'HuKangrui', 'LiuHuijun', 'ZhangShenghong'],
			['LiZhijian', 'ZhangXiaoying', 'ShiQianyi', 'ZhuoJiaming', 'ChenAnran', 'LiRuxian'],
			['GaoYichen', 'HuangYiheng', 'LiXingrong', 'WuShiqi', 'Mengruolin', 'XieChen']]
lisnum_gs = [['Dl5','Dl6','Dl8','Dl9'],['Dl5','Dl6','Dl8','Dl9'],['Dl5','Dl6','Dl8','Dl9']]

em = date.today()
curdate = '%s.%s.%s'%(em.year,em.month,em.day)




def generate_for_lis_groups(gpNamel,lis_nums,data_object):
	'''	input: gp --> a list containing all the names inside a group
				lis_num --> a list containing all numbers to be test_student

		output: list containing all information to be printed
	'''
	output = []
	for name in gpNamel:
		for lis_num in lis_nums:
			a = student_vocab_list(name,lis_num,data_object)
			output.append(a.generate_list())
	return output




def generate_list_specific(name_gs,groups,lisnum_gs,data_object,date = curdate, subdirectory = ''):
	'''generate all txt files need for testing, with name in name_gs+date  as filename'''
	print date
	for identifier, group, lisnums in zip(name_gs,groups,lisnum_gs):
		data = generate_for_lis_groups(group,lisnums, data_object)
		print data
		a = vocabulary_tests_data(data,date)
		if len(subdirectory) ==0:a.output(subdirectory + identifier+date)
		else: a.output(subdirectory +'/' +identifier+date +'.txt')

#generate_list_specific(name_gs,groups,lisnum_gs,mydata,subdirectory = '/Users/Zhe/Desktop/testing')


