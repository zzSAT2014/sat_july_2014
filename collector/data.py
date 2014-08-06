#access to modules in the upper level, mainly dictionary from word bank
import sys


#access to current level
import os
subdir = os.path.dirname(__file__)
sys.path.append(subdir)

sys.path.append(os.path.abspath(os.path.join(subdir, os.pardir)))

import shelve
sopen = lambda filename: shelve.open(filename,writeback = True)

import re
from copy import deepcopy

from print_dict import print_dict

class data(object):
	def __init__(self,filename,mode = 'db'):
		'''opens up the file in r+ mode, unless otherwise specified, i.e use a+ to create file'''
		if mode is 'normal':
			self.file = open(filename,mode = 'r+')
			string = ''
			for line in self.file:
				string = eval(line)
		elif mode is 'db':
			self.file = sopen(filename)
			string = eval(repr(self.file))
		self.name = filename
		# string=self.file.read().strip()
		
		#print 'hi'
		#print string
		self.info =  string
		self.file.close() #must close file to avoid corruption


	def update(self, func, output = None):
		'''modify the input and save it'''
		def write2db(mydict,dbfile):
			for key,value in mydict.items():
				#print key,'\n',value
				dbfile[key] = value
		try:
			if output == None: output = self.name
			func(self.info)
			#print_dict(self.info)
			print output
			self.dbfile = sopen(output)
			print 'hi'

			#print self.info
			#print self.info
			write2db(self.info,self.dbfile)
			print 'updating'
		finally:
			self.dbfile.close()
			print 'finish update'

	def get_student(self,name):
		'''return all information about the student'''

		#print_dict(self.info[name])
		if name in self.info: return self.info[name]
		else: return {}
	def remove(self,parent_dir,dir_key,output = 'newmaster'):
		'''parent_dir <--- a list of directories
			dir_key <--- field to be remove_field

			remove indicated field of all students and output the file using update'''

		fun = remove_field(parent_dir,dir_key)
		self.update(fun,output = output)

	def __str__(self):
		
		
		print_dict(self.info)
		
		return 'end'


#####used to remove specific parts of data, data manipualtion
def access_subdirectory(dir,dictionary):
	if len(dir) == 0: return dictionary
	else: 
		#print '\tline 13 %s'%dir
		curkey,furkey = dir[0],dir[1:]
		if curkey in dictionary: return access_subdirectory(furkey,dictionary[curkey])
		else: return None 

def test_access_subdir():
	a= {1:{2:{4:5},'none':2}}
	print access_subdirectory([1,2,4],a)
	if not access_subdirectory([1,2,5],a): print 'hello world'
	b= access_subdirectory([1,2],a)
	print b
	del b[4]   
	print a

#test_access_subdir()

def remove_field(parent_dir,dir_key):
	'''destined_dir: a list containing all sub-directory to find required a field'''
	def inner(dictionary):
		for student in dictionary:
			if not access_subdirectory(parent_dir,dictionary[student]): print 'oops not here'
			if access_subdirectory(parent_dir,dictionary[student]): 
				subdict = access_subdirectory(parent_dir,dictionary[student])
				print 'validation%s'%(dir_key in subdict)
				if dir_key in subdict:
					print 'remove%s'%(subdict[dir_key])
					del subdict[dir_key]
		print 'removing.........'
	print 'building deleter'
	return inner

def test_data():
	#a= data('empty')
	
	input_file = '/Users/Zhe/Desktop/sat_july_2014/data_2014.07.15/test'
	a = data(input_file)
	print a

alldata = data('/Users/Zhe/Desktop/sat_july_2014/data/database1')
#alldata.remove([],'CRpractice')
#test_data()