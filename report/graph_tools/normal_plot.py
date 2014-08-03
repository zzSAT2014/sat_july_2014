from pylab import *

def normal_plot(data, xlabels, tit, outputdir, xaxis = None, yaxis = None):
	'''input:
		data <--- dictionary: {'zhe':[1,2,3,4,5],'zhang':[6,7,8,9,10]}
		xlabels <--  a list of stings : e.g. ['day1','day2','day3','day4','day5']
		tit <--- title
		outputdir : output directory

	output:
		a graph to the destined file'''

	a = figure(figsize = (6,6) )
	for value in data.values():
		temp = len(value)
	if xaxis: xlabel(xaxis)
	if yaxis: ylabel(yaxis)


	title(tit)
	defaultlen = len(xlabels)
	_axis = range(defaultlen)
	xticks(_axis,xlabels)

	for key,value  in data.items():
		if not len(value) == defaultlen: 
			print 'input data error,no graph generated, check agian'
			return None
		plot(_axis,value,'-o',label = key)
	legend(loc = 'upper left')

	output = outputdir + '/'+tit
	a.savefig(output)
	show()
	print 'graph (%s) successfully drawn & saved' %tit

def test_normal_plot():
	data = {'zhe':[1,2,3,4,5],'zhang':[6,7,8,9]}
	xlabels = ['day1','day2','day3','day4','day5']
	tit = 'test_normal_plot'
	outputdir = '/Users/Zhe/Desktop/draw_trial'
	normal_plot(data, xlabels, tit, outputdir)

#test_normal_plot()