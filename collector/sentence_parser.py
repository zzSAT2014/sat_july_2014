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
from word_bank import dictionary
from data import data
from parser import txt_parser
from collections import defaultdict

def correctness_update(info,input):
	'''input <-- information (correctness,{correct:[lisnums....],wrong:[lisnums.....]}
				<--(Bool,lisnum)

	output ----> information (correctness,{correct:[lisnums],wrong:[lisNums]})'''

	inputBool, inputSen = input 
	inputBool = eval(inputBool)
	if len(info) == 0: return (1,{'correct':[inputSen],'wrong':[]}) if inputBool else (0,{'correct':[],'wrong':[inputSen]})
	else: 
		_,information = info 
		corrects = information['correct'][:]

		wrongs = information['wrong'][:]
		if inputBool: corrects.append(inputSen)
		else: wrongs.append(inputSen)
		numcorrects = len(corrects)
		tottested = len(wrongs)+numcorrects
		correctnessRate = numcorrects/float(tottested)
		return (correctnessRate,{'wrong':wrongs,'correct':corrects})

find_average = lambda lis: sum(lis)/float(len(lis))


def clause_update(info,input):
	'''input <--- info : (average_correctness,[(correctness,lisnum)....])
					input :(correctness, lisnum)


		output ---> num_info (new_average_correctness,[(correctness,lisNum).....+])'''

	pick_0 = lambda tup: tup[0]
	inputCor,inputLis = input
	if len(info)==0: return (inputCor,[input])
	_, information = info
	information.append(input)
	#print information
	all_cor=map(pick_0,information)

	#print all_cor
	return (find_average(all_cor),information)


def sentence_info_update(func):
	'''input <--- function used to update

	output ---> update function'''

	def inner(input):
		'''user specific input type
					(correctness, lisnum) for clause_update
					(Bool,lisnum) for correctness_update'''

		def real_inner(tup):
			'''update the user information using function'''
			return func(tup,input)
		return real_inner
	return inner


update_clause = sentence_info_update(clause_update)
update_correctness = sentence_info_update(correctness_update)




def word_add(date):
	'''appending function with stuff to be appended as function constructor, x'''
	def inner(tup):
		'''input <--- tup <---- (number of times,[dates......]

		output ---> number +1,[dates....+]'''
		
		num,dates = tup
		dates.append(date)
		return (len(dates),dates)
	return inner





def index_2_word(lisNum):
	'''translate index to word
	set lisNum

	output ---> inner function
	'''

	def inner(coor):
		'''input <--- coordiantes

		output ---> word'''
		return (lisNum,coor)
	return inner

# l_trans=index_2_word('l5')
# print l_trans('D2')

class sentence_parser(txt_parser):
	def __init__(self,filename):
		'''custom designed vocab template processing toool'''
		self.file = open(filename,'r')
		self.temp = {}
		self.info = []#(flag(wheter it is append),directory,result)

	def parser(self):
		regex = re.compile('[A-Za-z]')
		def inner(dic):
			for index,line in enumerate(self.file):
				if index == 0: date=line.split()[1] #get dates
				elif index == 1: continue
				else:

					if not re.match(regex,line): continue
					print line 
					name,sentenceNum,extraction,structure,clause,word,phrase  = line.split()
					s_trans = index_2_word(sentenceNum)  #translate to sentence unique identifier used later for direct referrence for specific parts
														#i.e (S1,3), (S2,2.1)  could update to real clause, but not necessary  

					# tested = map(l_trans,re.split(',',tested) ) #translate to word ,	all clauses to be tested
					#data type conversion

					phrase = phrase.split(',') 
					clause = clause.split(',') 
					word = word.split(',') 

					if phrase == ['None']: phrase = []
					if clause == ['None']: clause = []
					if word == ['None']: word = []
					#print 'line 149 word is \t%s' %word
					#print 'line 150 phrase under test is\t%s'%phrase
					phrase_sub = lambda string: re.sub('_',' ',string)
					phrase = map(phrase_sub,phrase)

					clause = map(s_trans,clause)

					#convert to valid input data

					clause_correctness = len(clause)	#****************************************	update to real correctness rate when possible		  					
					#possible support for percentage of correct clauses when sentence bank is established
					# if len(wrong) >0: wrong = map(l_trans,re.split(',',wrong))	#translate to word
					# correct = [a for a in tested if a not in wrong]#maybe i will add untested word later

					#conversion to usable data type

					

					#date specific, to track students's progress by date
					sub_dict(dic,[name,'sentence','date',date,'absorption'],func = update_clause((clause_correctness,sentenceNum)),value=()) #date specific : date:[(listNum,correctRate).....] appender
					#print dic
					sub_dict(dic,[name,'sentence','date',date,'extraction'],func = update_correctness((extraction,sentenceNum)) ,value=()) #list specific : lisNum:[(date,correctRate).....] appender
					#print dic

					#track all phrases and words

					for identi,cate in zip(['word','phrase'],[word,phrase]):    #word specific: word: wrong : (numdates,[....]), correct : (numdates,[....]), mostRecent : (flag,date)
						for atom in cate: #for word in each category
							#translate(word)
							sub_dict(dic,[name,'sentence',identi,atom],func = word_add(date) ,value = (0,[]))
					for identi,cate in zip(['structure','extraction','phrase','clause','date'],[structure,extraction,phrase,clause,date]):		
						sub_dict(dic,[name,'sentence',sentenceNum,identi],value = cate)
		return inner

def test_sentence_parser():
	print subdir
	# data_file = '/Users/Zhe/Desktop/sat_july_2014/data_2014.07.15/test'
	data_file = subdir + '/'+'empty'
	input= 'sentence_parser_template'

	original = data(data_file)
	a = sentence_parser(subdir + '/'+input).parser()

	original.update(a,output = 'test_output')
	print original
	#empty={}
	#a(empty)
	#print_dict(empty)

#test_sentence_parser()
#test_vocab_parser()
