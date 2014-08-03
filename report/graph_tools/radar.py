import pygal
from pygal.style import BlueStyle

def radar(data, labels, tit, outputdir):
	'''input:
		data <--- a dicytionary person: his data  {'zhe':[1,2,3],...} normalized to 100 values should have the same length
		labels <--- a list of strings of his quality ['intelligence','emotional stability',....]
		tit <--- title as a strings
		outputdir <---  directory for the output folder

	output: ---> a svg graph at destined folder'''
	
	radar_chart = pygal.Radar(style = BlueStyle)
	radar_chart.title = tit
	radar_chart.x_labels = labels
	defaultLen = len(labels)


	for key,values in data.items():
		if not len(values) == defaultLen: 
			print 'input value does have the correct length, aborting drawing'
			return None

		radar_chart.add(key,values)
	radar_chart.add('max',len(values)*[100,])
	output = outputdir + '/'+tit + '.svg'
	radar_chart.render_to_file(output)

	print 'figure (%s) successfully drawn & saved' %tit

def test_radar():
	labels =  ['sentence structure','sentence extraction','paragraph','vocab','extraction']
	data = {'zhe':[60, 70, 80,50, 20], 'average':[50,60,30,80,90],'zhi':[80,]*5}
	outpudir = '/Users/Zhe/Desktop/draw_trial'
	tit = 'test_radar'
	radar(data,labels,tit,outpudir)
#test_radar()