#this module computes the percentage of progress for each individual studetn
import sys
#access to current level files
import os
subdir = os.path.dirname(__file__)
sys.path.append(subdir)

sys.path.append(os.path.abspath(os.path.join(subdir, os.pardir)))


from collections import defaultdict
from mydata import mydata
from tools import dates_before
from tools import average
from mydata import print_dict
from graph_tools import pie_chart
from graph_tools import stacked_bar
from graph_tools import normal_plot 
from mydata import systoday
from mydata import sub_dict

take_latest = lambda x: x[-1]
def compute_accuracy(listup):
	'''input <-- a list of tuples i.e. [(Bl1, 0.1), (Bl2,0.3)...]
				i.e. self.past self.progrss, self.all
	output: --> a number indicating accuracy'''
	all_accuracy = []
	for tup in listup:
		all_accuracy.append(take_latest(tup))

	return average(all_accuracy) 

#does not support tracking of progress as of now
def list_compare(lisnum):
	'''input<--listnumber

	output--> a tuple for comparision i.e. (1,20) 1<-- direct_hits ; 20 <-- current list'''

	identi, num = lisnum[:2], eval(lisnum[2:])
	if identi == 'Dl': key = 1
	elif identi == 'Bl': key =2
	elif identi == 'Xl' : key =3
	return (key,num)

def convert_to_set(vocab_list):
	'''input: vocab_list [('Bl1', 1.0), ('Bl2', 1.0), ('Bl3', 1.0), ('Bl4', 0.9), ('Dl7', 1.0), ('Dl9', 1.0), ('Dl10', 0.9), ('Dl5', 1.0), ('Dl6', 0.9), ('Dl7', 0.9), ('Dl8', 1.0), ('Dl9', 1.0), ('Dl10', 1.0)]

	output <-- a set containing all list numbers i.eset([Bl1,Bl2,Bl3])'''
	take_first = lambda tup: tup[0]
	lis = map(take_first,vocab_list)
	return set(lis)

#print convert_to_set([('Bl1', 1.0), ('Bl2', 1.0), ('Bl3', 1.0), ('Bl4', 0.9)])
def gen_list(tag):
	lis = []
	def inner(start,end):
		for i in range(start,end+1):
			lis.append(tag+str(i))
		return lis
	return inner


def choose_list(identi):
	def inner(lisnum):
		return identi == lisnum[:2]
	return inner


def compute_finished(vinfo):
	'''input <-- vocab_student object containing all relevent inof about a student

	output: 
			--> a dictonary containing {direct_hits: (finished, progrss, unfinished) * number of list for each group }
			--> percentage of finished as of now'''
	past = convert_to_set(vinfo.past)
	progress = convert_to_set(vinfo.progress).difference(past)
	start = min(progress, key=list_compare)
	end = max(progress,key =list_compare)
	recent_change = (start,end)
	present = convert_to_set(vinfo.all)

	Bl = gen_list('Bl')
	Bl = Bl(1,20)

	Xl = gen_list('Xl')
	Xl = Xl(1,86)

	Dl = gen_list('Dl')
	Dl = Dl(1,10)

	all_List = Dl[:]
	all_List.extend(Bl)
	all_List.extend(Xl)

	totnum = len(all_List)
	start_index = all_List.index(start)
	done = all_List[:start_index]
	end_index = all_List.index(end)
	waiting = all_List[end_index+1:]
	progress = all_List[start_index: end_index+1]

	data = defaultdict(dict)
	for cate in ['Bl','Xl','Dl']:
		tester = choose_list(cate)
		for identi,group in zip(['done','progress','waiting'],[done,progress,waiting]):

			templist = filter(tester,group)
			if len(templist) > 0: data[cate][identi] = (len(templist))
	past = len(done) / float(totnum) *100
	current = (len(done)+len(progress)) / float(totnum) *100
	return (data,past,current)

def create_label(dic):
	'''customer desigened function to be used in the module only

	input <--- {'Bl': {'progress': 8, 'waiting': 12}, 'Dl': {'done': 10}, 'Xl': {'waiting': 86}}

	ouput ---> (label_list, data, emphasis)'''
	output = ()
	lable_list = []
	data = []
	emphasis = []
	count = 0

	for listname in ['Dl','Bl','Xl']:
		value = dic[listname]
		#print value
		for type2 in ['done','progress','waiting']:
			
			if type2 in value:
				newvalue = value[type2]
			
				lable_list.append(listname +' '+ type2)
				#print 'hi\t%s'%lable_list
				data.append(newvalue)
				if type2 == 'progress':
					emphasis.append(count)
				count +=  1
	print lable_list
	return (lable_list, data, emphasis)


take_date = lambda tup: tup[0]

list_convert = lambda dickey, dicvalue: (dickey,dicvalue[1])


class vocab_student(object):
	def __init__(self,student_name, output ='/Users/Zhe/Desktop/sat_july_2014/report/vocab_processing', delta = 15):
		self.outputdir = output
		self.name = student_name
		self.info = mydata.info[student_name]['vocab']
		self.sinfo = mydata.info[student_name]
		self.delta = 3
		self.dates = dates_before(delta,systoday)
		self.progress = []
		self.past = []
		self.all = []
		for date in self.dates:
			if date in self.info['date']:

				self.progress.extend(self.info['date'][date])
		
		for lis in self.info['list']:
			value = self.info['list'][lis]
			self.all.append( list_convert(lis, take_latest(value)) )

			if take_date(take_latest(value)) not in self.dates:
				self.past.append( list_convert(lis, take_latest(value)))

			elif len(value)>1:
				self.past.append( list_convert(lis, value[-2]))
		self.processing()
		self.draw_graph()
	def processing(self):
		print 'processing'
		self.info['quality']={}
		self.info['quality']['past'] = compute_accuracy(self.past)
		self.info['quality']['progress'] = compute_accuracy(self.progress)
		self.info['quality']['current'] = compute_accuracy(self.all)

		self.info['quantity'],past, current = compute_finished(self)
		self.info['quantity'] = create_label(self.info['quantity'])

		sub_dict(self.sinfo, ['aggregate','past', 'vocab'] ,func=lambda x: past *  self.info['quality']['past'] )
		sub_dict(self.sinfo, ['aggregate','current', 'vocab'] ,func=lambda x: current * self.info['quality']['current'])

		print self.sinfo['aggregate']
		print 'finish processing'
		print_dict(self.info['quantity'])

	def draw_graph(self):
		output = self.outputdir
		labels, fracs, emphasis = self.info['quantity']
		tit = self.name +'vocab_quantity'
		print tit
		pie_chart(fracs,labels,tit,output,emphasis = emphasis,show = False)

		quality = self.info['quality']

		print quality
		tit = self.name + 'vocab_accuracy'
		stacked_bar( {self.name:quality.values()}, quality.keys(), tit, output)
	def update(self, output= None):
		if not output:
			mydata.update(lambda x:x)
		else: 
			mydata.update(lambda x:x, output =output)


# a = vocab_student('QianyiShi')

#a.update(output = '/Users/Zhe/Desktop/sat_july_2014/report/vocab_processing/testing')



