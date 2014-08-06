import sys
#access to current level files
import os
subdir = os.path.dirname(__file__)
sys.path.append(subdir)
#access to super level
sys.path.append(os.path.abspath(os.path.join(subdir, os.pardir)))

from timeapi import dates_before
from timeapi import systoday
def average(list):
	'''input: a list of values

	output: avergae value of the iterable'''
	if len(list) == 0: return 0

	return sum(list)/float(len(list))

#print average([1,2,3])