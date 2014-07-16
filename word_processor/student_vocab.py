#access from super level
import sys
sys.path.append('/Users/Zhe/Desktop/sat_july_2014')

from pprint import pprint
#pprint(sys.path)

import re
import os
subdir = os.path.dirname(__file__)
sys.path.append(subdir)

from word_bank import dictionary

#access collector from upper level

from weighted_random import weighted_choice
from student import student
from eval_weight import *

from collector import mydata
from collector import sub_dic
sub_dict = sub_dic.sub_dict

class student_vocab(student):
	'''reduce to student_vocab
	{vocab:blah,blah} ---> {blah,blah}'''

	def __init__(self,name):
		student.__init__(self,name)
		if 'vocab' not in self.info:#fail safe
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
			self.dateC = {}   #---> [(date,correctness)]
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

def test_student_vocab_list():
	a = student_vocab_list('LiZhijian','Dl5')
	print a.list
#test_student_vocab_list()

