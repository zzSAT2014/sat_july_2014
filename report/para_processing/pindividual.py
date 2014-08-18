#this module computes the percentage of progress for each individual studetn
import sys
#access to current level files
import os
subdir = os.path.dirname(__file__)
sys.path.append(subdir)

sys.path.append(os.path.abspath(os.path.join(subdir, os.pardir)))

extract_from_tuple = lambda tup : tup[1]
get_list =  lambda date_dic : map(extract_from_tuple,date_dic['correctness'][1])

from mydata import mydata
from mydata import data
from tools import dates_before
from tools import dates_before
from tools import average
from mydata import systoday
from mydata import print_dict
from graph_tools import pie_chart
from graph_tools import normal_plot
from mydata import sub_dict

#print mydata
class cr_practice_student(object):

	def __init__(self,student_name, output =  '/Users/Zhe/Desktop/sat_july_2014/report/para_processing',delta = 5, recent = 2):
		self.name = student_name
		self.info = mydata.info[student_name]['CRpractice']
		self.sinfo = mydata.info[student_name]
		self.output =output
		#print_dict(self.info)
		self.delta = delta
		self.dates = dates_before(delta,systoday)
		self.recent = dates_before(delta*recent,systoday)
		self.progress = []
		self.past = []
		self.all = []
		for date in self.dates:
			if date in self.info['date']:
				#print 'hi'
				self.progress.extend(get_list(self.info['date'][date]))
		#self.recent = 
		self.progressNum = len(self.progress)
		
		self.tot = 50 #total number of excercises

		

		datesinfo = self.info['date']
		self.all = []
		for date in datesinfo:
			self.all.extend(get_list(datesinfo[date]))
		self.allNum = len(self.all)
		#print self.all
		sub_dict( self.sinfo, ['aggregate','past', 'practice quantity'] ,func=lambda x: 100/float(self.tot) * (self.allNum - self.progressNum) )
		sub_dict( self.sinfo, ['aggregate','current', 'practice quantity'], func = lambda x: 100/float(self.tot) * (self.allNum))

		self.draw_graph()

		

	def processing(self):
		print 'processing'
		self.info['quality']={}
		self.info['quality']['past'] = compute_accuracy(self.past)
		self.info['quality']['progress'] = compute_accuracy(self.progress)
		self.info['quality']['current'] = compute_accuracy(self.all)

		self.info['quantity'],past, current = compute_finished(self)
		self.info['quantity'] = create_label(self.info['quantity'])
		self.info['aggregate'] ={}
		self.info['aggregate']['past'] = past *  self.info['quantity']['past']
		self.info['aggregate']['current'] = current * self.info['quantity']['current']
		print 'finish processing'
		print_dict(self.info['quantity'])

		

	def draw_graph(self):

		#draw pie chart to show progress
		output = self.output
		labels, fracs, emphasis = ['done','progress','waiting'], [self.allNum - self.progressNum, self.progressNum, self.tot], [1]
		print fracs
		tit = self.name+'  ' +'para_quantity'
		print tit
		pie_chart(fracs,labels,tit,output,emphasis = emphasis,show = False)

		#draw correctness of progress

		cordata = {self.name:[]}
		corsub = cordata[self.name]
		extdata = {self.name:[]}
		extsub = extdata[self.name]
		xlabels = []
		for serialNum in self.progress:
			corsub.append(self.info[serialNum]['correctness'])
			extsub.append(self.info[serialNum]['extraction'][0])
			xlabels.append(serialNum)
		tit = self.name+'  ' +'most_recent_correctness'


		print 'computing understaning aggregate'
		

		if 'understanding' not in self.sinfo['aggregate']['current']: self.sinfo['aggregate']['past']['understanding'] = 0
		
		else: self.sinfo['aggregate']['past']['understanding'] = self.sinfo['aggregate']['current']['understanding']
		self.sinfo['aggregate']['current']['understanding'] = 100 - 10*average(extsub)
		
		try: normal_plot(cordata, xlabels, tit, output, xaxis = None, yaxis = None)
		finally:
			tit = self.name + ' ' + 'most_recent_extraction'
			#print extdata
			normal_plot(extdata, xlabels, tit, output, xaxis = None, yaxis = None)

		info = self.info['date']
		cordata = {self.name:[]}
		corsub = cordata[self.name]
		extdata = {self.name:[]}
		extsub = extdata[self.name]
		self.recent.reverse()
		dates = []
		for date in self.recent:
			if date in info:
				dates.append(date)
				corsub.append(info[date]['correctness'][0])
				extsub.append(info[date]['extraction'][0])
		xlabels = dates
		tit = self.name+'  ' +'dates_recent_correctness'
		normal_plot(cordata, xlabels, tit, output, xaxis = None, yaxis = None)
		tit = self.name + ' ' + 'dates_recent_extraction'
		normal_plot(extdata, xlabels, tit, output, xaxis = None, yaxis = None)
		# quality = self.info['quality']

		# print quality
		# tit = self.name + 'vocab_accuracy'
		# stacked_bar( {self.name:quality.values()}, quality.keys(), tit, output)
	def update(self):
		mydata.update(lambda x:x,output = '/Users/Zhe/Desktop/sat_july_2014/report/vocab_processing/testing')
 
#a = cr_practice_student('Zhe')
#a.update()

