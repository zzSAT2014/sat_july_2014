from datetime import date
#custom designed functions
###############################################################################################to be changed later
# eval_most_recent = lambda flag,date: 1
# eval_wrong = lambda num, dates: 1
# eval_correct = lambda num, dates: 1



def time_duration(most_recent_date):
	'''Calculate the time between the date of last test and current date'''
	today = date.today()
	past= most_recent_date.split('.')
	past = map(int, past)
	past = date(*past)
	if date ==None:
		time_duration = 0
	else:
		time_duration = today - past
	return time_duration.days



def eval_most_recent(flag, time, weighting_factor=10):
	'''evaluate weighting_factor according to most recent test'''
	time = time_duration(time)
	if flag == False:
		weighting_factor = weighting_factor+ 2*time
	else:
		weighting_factor = max(weighting_factor - 100/float(time),0)
	return weighting_factor


def eval_wrong(num,dates,weighting_factor=10):
	'''evaluate weighting_factor according to total number of wrong answers to a word'''
	if num ==0:
		weighting_factor -= 5
	else:
		weighting_factor += num*5
	return weighting_factor


def eval_correct(num,dates,weighting_factor=10):
	'''evaluate weighting_factor according to total number of right answers to a word'''
	weighting_factor -= num*5
	return weighting_factor


def weight_word(dic ,untested = 30):
	'''evaluate all the contents of the dic and return a weight value
	input <--:dic --> sucdictionary belonging to the word, includes {correct,wrong,mostRecent}


	output --> a numerical word'''
	if dic is None:
		return untested
	else: 
		weight = 0
		components = ['correct','wrong','mostRecent']
		evalfuncs = [eval_correct, eval_wrong, eval_most_recent]
		for ele,func in zip(components,evalfuncs):
			if ele in dic:
				#print 'ele is -->%s\t, func  is %s' %(ele,func)
				#print '\t testing weighted_word-->%s' %(func(*(dic[ele])))
				#print type
				weight +=  func(*(dic[ele]))
		return weight


