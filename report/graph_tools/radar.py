import pygal
from pygal.style import BlueStyle

def radar(data, labels, tit, outputdir):
	'''input:
		data <--- a dicytionary person: his data  {'zhe':[1,2,3],...} normalized to 100 values should have the same length
		labels <--- a list of strings of his quality ['intelligence','emotional stability',....]
		tit <--- title as a strings
		outputdir <---  directory for the output folder

	output: ---> a svg graph at destined folder'''
	
	radar_chart = pygal.Radar()#style = BlueStyle)
	radar_chart.title = tit
	radar_chart.x_labels = labels
	defaultLen = len(labels)


	for key,values in data.items():
		if not len(values) == defaultLen: 
			print 'input value does have the correct length, aborting drawing'
			return None

		radar_chart.add(key,values)
	radar_chart.add('max',
		(len(values)-1)*([0,])+[100,])

	output = outputdir + '/'+tit + '.svg'
	radar_chart.render_to_file(output)

	print 'figure (%s) successfully drawn & saved' %tit

def test_radar():
	labels =  ['vocab','practice quantity','understanding','score','grammer','essay','sentence completion']
	data = {'past':[40,20,60,45,45,40,50], 'average':[60,25,50,57,50,45,45],'current':[90,75,80,70,60,50,90]}
	outpudir = '/Users/Zhe/Desktop/'
	tit = 'SAT ability aggregate report'
	radar(data,labels,tit,outpudir)
test_radar()