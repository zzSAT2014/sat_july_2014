
import sys

__all__ = ['generate_list_specific']
__doc__ = '''generate_list_specific <--- name_gs  <--- group name identifier
														e.g. ['sb','notsb1','notsb2']

										groups  <--- name of students inside a group
														e.g.[['ZhangJianxin', 'GuoZiwei', 'ZhouMingrui', 'ChenYanghui', 'GaoYueMing', 'HuKangrui', 'LiuHuijun', 'ZhangShenghong'],
														['LiZhijian', 'ZhangXiaoying', 'ShiQianyi', 'ZhuoJiaming', 'ChenAnran', 'LiRuxian']] 
										lisnum_gs <--- lists to be tested
														e.g.[['Dl5','Dl6','Dl8','Dl9'],['Dl5','Dl6','Dl8','Dl9']] 
										data_object 
										date = curdate
										 subdirectory = <-- subdirectory folder for output
										 					e.g.  '/Users/Zhe/Desktop/testing'''
#access to current level
import os
subdir = os.path.dirname(__file__)
sys.path.append(subdir)

#access to super level
sys.path.append(os.path.abspath(os.path.join(subdir, os.pardir)))


from student_vocab import student_vocab_list
student_vocab_list

from generate_vocab_lists import generate_list_specific
generate_list_specific

