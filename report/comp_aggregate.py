import sys
#access to current level files
import os
subdir = os.path.dirname(__file__)
sys.path.append(subdir)

sys.path.append(os.path.abspath(os.path.join(subdir, os.pardir)))

from collector import mydata
from collector import print_dict
from tools import systoday
from collector import data
from collector import sub_dict
from collector import access_subdirectory
from vocab_processing import vocab_student
from para_processing import cr_practice_student
from graph_tools import radar


#computes aggreagte score from first CR result
#['aggregate','score','past'] ['aggreagte','score','current']
class student(object):

	def __init__(self,stu_name, outputdir = None):
		''' stu_name <--- str : name of a student'''
		self.info = mydata.get_student(stu_name)
		self.name = stu_name
		self.outputdir = outputdir
		#print self.info['SAT']
		score = eval(access_subdirectory(['SAT','FirstTest','CR'],self.info))
		# print scoer
		if score == None: score = 0
		score = score/ float(8)

		sub_dict(self.info, ['aggregate','past','score'] ,func=lambda x:score)
		sub_dict(self.info, ['aggregate','current','score'] ,func=lambda x:score)
		vocab_student(stu_name, output =outputdir)
		cr_practice_student(stu_name, output = outputdir)
		print self.info['aggregate']

		#draw graph
		aggr = self.info['aggregate']

		past = aggr['past'].values()
		cur = aggr['current'].values()
		labels = aggr['past'].keys()
		data = {'past':past,'current':cur}
		tit = 'ability summary'

		radar(data, labels, tit, outputdir)

	def draw_graph(self):pass
		

	def update(self, output= None):
		if not output:
			mydata.update(lambda x:x)
		else: 
			mydata.update(lambda x:x, output =output)

lis = ['AnranChen','ChenXie','HaoranLiao','MingruiZhou','QianyiShi','RuolinMeng','RuxianLi','ShiqiWu','XiaoyingZhang','XinrongLi','YuemingGao','ZhijianLi']
lis = ['HaoranLiao']
for studentname in lis:
	subdie = '/Users/Zhe/Desktop/sat_july_2014/report/data/'
	#os.mkdir(subdie + studentname)
	outputdir =subdie + studentname
	
	a = student(studentname,outputdir = outputdir)
	




