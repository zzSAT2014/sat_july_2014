import pygal
from pygal.style import LightGreenStyle
style = LightGreenStyle

def stacked_bar(data, x_labels, tit, outputdir):
	'''input:
		data <--- a dicytionary person: his data  {'zhe':[1,2,3],...} normalized to 100 values should have the same length
		xlabels <--- a list of strings of his quality ['intelligence','emotional stability',....]
		tit  <-- title of output file
		output directory


	output:
		print error message if field lengths do not match
		else draw graph''' 
	stackedbar_chart = pygal.StackedBar(style = style)
	stackedbar_chart.title = tit
	stackedbar_chart.x_labels = x_labels
	defaultLen = len(x_labels)

	for key,value in data.items():

		if not len(value) == defaultLen: 
			print 'input value does have the correct length, aborting drawing'
			return None

		stackedbar_chart.add(key,value)
	output = outputdir + '/'+tit + '.svg'
	stackedbar_chart.render_to_file(output)

	print 'figure (%s) successfully drawn & saved' %tit

def test_stacked_bars():
	labels =  ['sentence structure','sentence extraction','paragraph','vocab','extraction']
	data = {'zhe':[60, 70, 80,50, 20], 'average':[50,60,30,80,90],'zhi':[80,]*5}
	outpudir = '/Users/Zhe/Desktop/draw_trial'
	tit = 'test_stacked_bars'
	stacked_bar(data,labels,tit,outpudir)

#test_stacked_bars()