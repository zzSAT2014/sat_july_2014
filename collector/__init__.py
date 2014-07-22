import sys
#access to current level files
import os
subdir = os.path.dirname(__file__)
sys.path.append(subdir)


#access to modules in the upper level, mainly dictionary from word bank

sys.path.append(os.path.abspath(os.path.join(subdir, os.pardir)))


__all__=['data']
__doc__ = '''data <--- original information txt input
					output ---> data object, with update, get_student methods
			basic_parser <--- input input_filename
					basic_parser.parser() ---> parser function, used in combination with update methods
			vocab_parser <-- vocabulary input_filename
				vocab_parser.parser() -----> vocab_parser function, used with update methods
			print_dict
			sub_dict'''

#access to current level
import os
subdir = os.path.dirname(__file__)
sys.path.append(subdir)




from data import data
#original data 
data 
mydata = data(subdir +'/'+'test_output')
from sub_dic import sub_dict
sub_dict

from parser import basic_parser
basic_parser

from vocab_parser import vocab_parser
vocab_parser

from sub_dic import sub_dict
sub_dict

from mock_test_parser import CRmock_parser
CRmock_parser

from print_dict import print_dict

from sentence_parser import sentence_parser