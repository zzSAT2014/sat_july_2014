from pylab import *

def pie_chart(fracs,labels,tit,outputdir,emphasis = None,show = False):
	''' fracs <-- a list of numbers  [1,2,3,4..]
		labels <--- a list of labels for each slices ['fuck','bitch','gay','lesbian'..]
		tit <--- a string 
		outputdir <--- directory for the output folder
		emphasis <-- int for which chart to emphasis e.g. 2
					list slices to be emphasized simultaneously e.g [2,3]

		output --> None

		do: draws a pie chart'''


	a = figure(figsize =(6,6))
	ax = axes([0.1, 0.1, 0.8, 0.8]) #initialize fig

	if not len(fracs) == len(labels):
		print 'fracs & labels does not match, unable t0 draw graph'
	else: 
		numSlices = len(fracs)
		explode = [0,] * numSlices
		if type(emphasis) is int: explode[emphasis] = 0.10
		else: 
			for index in emphasis:
				explode[index] = 0.1
		pie(fracs, explode=explode, labels=labels,
		autopct='%1.1f%%', shadow=None)
		if show: a.show()
		title(tit)
		filename = outputdir + '/' + tit
		a.savefig(filename)
		print 'figure (%s) successfully drawn & saved' %tit

def test_piechart():
	fracs = [100,200,600,400,500]
	labels = ['1','2','3','4','5']
	emphasis  = [2,3]
	title = 'test_piechart'
	outputdir = '/Users/Zhe/Desktop/draw_trial'
	pie_chart(fracs,labels,title,outputdir,emphasis = emphasis)
#test_piechart()