print 'initiliaitzing word bank'


#makes module in this folder available 
import os
subdir = os.path.dirname(__file__)
import sys
sys.path.append(subdir)



#from pprint import pprint
#pprint(sys.path)



#useful information
import word_bank
__all__ = ['dictionary']
dictionary = word_bank.dictionary()

