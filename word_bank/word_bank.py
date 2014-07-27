import re
import sys
from collections import defaultdict
import os
subdir = os.path.dirname(__file__)





def print_dict(dic):
	separator = '-->'
	indentation = '    '
	#@trace
	def inner(dic,inlevel=0):
		if type(dic) is not dict: print indentation*inlevel+repr(dic)
		else:
			for key in dic:
				print indentation*inlevel + repr(key) + separator
				
				inner(dic[key],inlevel+1)
	inner(dic)


def read_file(file_name):
	"""
	read file and output data in the form of lists.

	"""
	with open(file_name) as f:
		data=f.readlines()
	regex = re.compile(r'[\t;]')
	for i in xrange(len(data)):
		data[i] = regex.sub(' ',data[i])
	return data

#print read_file("word_list")
        


def divide_list(data):
	"""
	Input: word list

	Output: split the word list

	"""
	word_list = []
	temp = []
	for i in xrange(len(data)):
		if "@List" in data[i]:
			word_list.append(temp)
			temp = []
		else:
			temp.append(data[i])
	return word_list

#print divide_list(read_file("word_list"))

def trans(row_num,col_num):
	'''translate column and row number into user_friendly number'''
	coltab = {1:'A',2:'B',3:'C',4:'D'}
	return coltab[col_num]+str(row_num)

def generate_dict(word_lists,identifier):
	"""
	input: a list of word list
	Output: a dictionary where the keys are tuples(list_num,row_num,col_num),
	and the values are the words.

	"""
	dict = {}
	ldict = defaultdict(list)
	for i in xrange(len(word_lists)):
	    list_num = i + 1
	    for j in xrange(len(word_lists[i])):
			row_num = j + 1
			words = word_lists[i][j].split()
			for k in xrange(len(words)):
				col_num = k + 1
				dict[(identifier+'l'+str(list_num),trans(row_num,col_num))] = words[k]
				ldict[identifier+'l'+str(list_num)].append(words[k])
	return dict,ldict


def reverse_dict(dic):
	new = defaultdict(list)
	for key,value in dic.items():
		new[value].append(key)
	return new


def combi_dict(a,b):
	return dict(list(a.items())+list(b.items()))

def choose_index(list,identifier):
	for choice in list:
		if choice[0][0] == identifier: return choice
	else: 
		print 'word is not here'
		return None

class dictionary(object):
	def __init__(self):
		self.data,self.ldata = generate_dict(divide_list(read_file(subdir+"/direct_hits")),'D')
		#print self.data
		tempdata, templdata =  generate_dict(divide_list(read_file(subdir+"/barron_800")),'B')
		self.data = combi_dict(self.data,tempdata)
		self.ldata = combi_dict(self.ldata,templdata)
		tempdata, templdata =  generate_dict(divide_list(read_file(subdir+"/barron_3500.txt")),'X')
		self.data = combi_dict(self.data,tempdata)
		self.ldata = combi_dict(self.ldata,templdata)
		#print '\tafter combining these two \t%s' %self.ldata['Bl2']
		self.rdata = reverse_dict(self.data)
	def get_w(self,index):
		return self.data[index]
	def get_i(self,word,identifier=None):
		return self.rdata[word]   if identifier == None else choose_index(self.rdata[word],identifier)
	def get_l(self,lis,id = None):
		return self.ldata[lis]


# a = dictionary()
#print a.get_w(('Dl6', 'B13'))
#print len(a.get_l('Dl4'))
#print a.get_w(('Dl5','D2'))
# # print a.get_i('na\xc3\xafve')
#print a.get_i('appreciate',identifier = "B")
#print a.get_i

	




















