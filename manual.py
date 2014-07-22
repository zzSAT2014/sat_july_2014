import collector
from collector import print_dict
#print collector.__doc__
#intial data need to be initialized 
filename = '/Users/Zhe/Desktop/sat_july_2014/data/data_2014.07.21/output14'

originalData = collector.data(filename)
#print originalData


from datetime import date
em = date.today()
curdate = '%s.%s.%s'%(em.year,em.month,em.day)
print curdate

inputfile = '/Users/Zhe/Desktop/sat_july_2014/data/data_2014.07.18/cindy'

outputfile = '/Users/Zhe/Desktop/sat_july_2014/data/data_2014.07.21/output15'

def update_data(inputfile,outputfile,parser):#parser should be imported from collector
	Parser = parser(inputfile)
	f = Parser.parser()
	originalData.update(f,output = outputfile)
	#print originalData
parser = collector.vocab_parser #collector.CRmock_parser#collector.vocab_parser #, collector.basic_parser collector.CRmock_parser, vocab_parser
#update_data(inputfile,outputfile,parser)
#print_dict(originalData.get_student(''))
#print originalData.get_student('JiamingZhuo')['Tel']
#print originalData.get_student('ZhijianLi')['Tel']
print_dict(originalData.get_student('RuolinMeng')) 
def print_tel(lis):
	for name in lis:
		print name + '\tTel\t:' + repr(originalData.get_student(name)['Tel'])

lis= ['RuxianLi','ChenXie','ShiqiWu']
#print_tel(lis)
#vocab update
# vocab_parser_filename = ''
# vocabParser = collector.vocab_parser(vocab_parser_filename)
# vocab_parser = vocabParser.parser()
# originalData.update(vocab_parser,output = outputfile)

# vocab update
# mock_parser_filename = '/Users/Zhe/Desktop/sat_july_2014/data/data_2014.07.17/mock_test'
# mockParser = collector.CRmock_parser(mock_parser_filename)
# mock_parser = mockParser.parser()
# originalData.update(mock_parser,output = outputfile)

# print originalData

# basic_parser_filename = '/Users/Zhe/Desktop/sat_july_2014/data/data_2014.07.14/basic_info_input'
# #basic information update

# basicParser = collector.basic_parser(basic_parser_filename)
# basic_parser = basicParser.parser()

# originalData.update(basic_parser,output = outputfile)

# print originalData


import word_processor
# #print word_processor.__doc__
generator = word_processor.generate_list_specific
output_dir = '/Users/Zhe/Desktop/sat_july_2014/data/data_2014.07.22'

name_gs =['Cindy']
groups = [['QianyiShi']]
lisnum_gs = [['Bl7','Bl8']]
# name_gs = ['group0','group1','group2','group3']
# groups = [[  'MingruiZhou', 'ChenXie','ZhiweiGuo'],['XinrongLi','RuxianLi'],['YuemingGao'],['ZhijianLi','ShiqiWu','AnranChen','XiaoyingZhang','RuolingMeng']]
# lisnum_gs =[['Dl1','Dl2','Dl7','Dl8'],['Dl7','Dl8'],['Dl5','Dl6','Dl9','Dl10'],['Bl1','Bl2','Bl3','Bl4']]


#generator(name_gs,groups,lisnum_gs,originalData, subdirectory =output_dir)
