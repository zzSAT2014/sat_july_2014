import sys
#access to current level files
import os
subdir = os.path.dirname(__file__)
sys.path.append(subdir)

from data import access_subdirectory
from data import alldata
info = alldata.info

lis = ['AnranChen','ChenXie','HaoranLiao','MingruiZhou','QianyiShi','RuolinMeng','RuxianLi','ShiqiWu','XiaoyingZhang','XinrongLi','YuemingGao','ZhijianLi']# all active students
#print len(lis)

def decide_score(sinfo):
	'''info <-- subdict containing all information of a student

	output --> int: sat score'''
	return eval(access_subdirectory(['SAT','FirstTest','CR'],
										sinfo))

info['scoregroup'] = {}

def decide_range(lower,upper,excp =False):
	def inner(score):
		 
		if not score and excp:
				return True
		else: return all([score >= lower, score < upper])
	return inner

def sift(tester,info = info):
	def inner(student_name):
		#print info
		score = decide_score(info[student_name])
		return tester(score)
	return inner


def select_group(lis):
	#for student
	group450 = decide_range(450,500,excp = True)
	group500 = decide_range(500,550)
	group550 = decide_range(550,600)
	for group,tester in zip(['450','500','550'],[group450,group500,group550]):

		criteria = sift(tester)
		info['scoregroup'][group] = filter(criteria,lis)
		for student in info['scoregroup'][group]:
			info[student].update({'group':group})

	print info['scoregroup']

select_group(lis)

for student in lis:
	print info[student]['group']
alldata.update(lambda x:x)

