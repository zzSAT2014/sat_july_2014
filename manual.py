import collector
from collector import print_dict
#print collector.__doc__
#intial data need to be initialized 
filename = '/Users/Zhe/Desktop/sat_july_2014/data/data_2014.07.23/output6'

originalData = collector.data(filename)
#print originalData


from datetime import date
em = date.today()
curdate = '%s.%s.%s'%(em.year,em.month,em.day)
print curdate

inputfile = '/Users/Zhe/Desktop/sat_july_2014/data/data_2014.07.14/basic_info_input'

outputfile = '/Users/Zhe/Desktop/sat_july_2014/data/data_2014.07.23/output7'

def update_data(inputfile,outputfile,parser):#parser should be imported from collector
	Parser = parser(inputfile)
	f = Parser.parser()
	originalData.update(f,output = outputfile)
	#print originalData
parser = collector.basic_parser
par_dir = ['CRmock']
key_dir = 'word'
originalData.remove(par_dir,key_dir,output = outputfile) #collector.CRmock_parser#collector.vocab_parser #, collector.basic_parser collector.CRmock_parser, 
#update_data(inputfile,outputfile,parser)
#print_dict(originalData.get_student(''))
#print originalData.get_student('JiamingZhuo')['Tel']
#print originalData.get_student('ZhijianLi')['Tel']
print_dict(originalData.get_student('XinrongLi')) 
def print_tel(lis):
	for name in lis:
		print name + '\tTel\t:' + repr(originalData.get_student(name)['Tel'])

lis= ['RuxianLi','ChenXie','ShiqiWu']



import word_processor
# #print word_processor.__doc__
generator = word_processor.generate_list_specific
output_dir = '/Users/Zhe/Desktop/sat_july_2014/data/data_2014.07.27'

# name_gs =
# groups = [['QianyiShi']]
# lisnum_gs = [['Bl7','Bl8','Dl9','Dl10']]
splitter = lambda string: string.split()
name_gs = ['JianxinZhang','YuemingGao','ShiqiWu','XiaoyingZhang','ZiweiGuo','MingruiZhou','RuolinMeng','ChenXie','AnranChen','QianyiShi','JiamingZhuo','ZhijianLi',
'XinrongLi','RuxianLi']
groups =  name_gs
convert = lambda a: [a]
groups = map(convert,groups)
print groups


#lisnum_gs = map(splitter,lisnum_gs)

#generator(name_gs,groups,lisnum_gs,originalData, subdirectory =output_dir)
#print_tel(name_gs)
