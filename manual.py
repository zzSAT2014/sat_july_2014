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

outputfile = '/Users/Zhe/Desktop/sat_july_2014/data/data_2014.07.23/output6'

def update_data(inputfile,outputfile,parser):#parser should be imported from collector
	Parser = parser(inputfile)
	f = Parser.parser()
	originalData.update(f,output = outputfile)
	#print originalData
parser = collector.basic_parser #collector.CRmock_parser#collector.vocab_parser #, collector.basic_parser collector.CRmock_parser, 
#update_data(inputfile,outputfile,parser)
#print_dict(originalData.get_student(''))
#print originalData.get_student('JiamingZhuo')['Tel']
#print originalData.get_student('ZhijianLi')['Tel']
#print_dict(originalData.get_student('RuolinMeng')) 
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
lisnum_gs =['Dl1 Dl2 Dl3 Dl4 Dl3 Dl4 Dl5 Dl6 Dl1 Dl2 Dl5 Dl6 Dl3 Dl4 Dl7 Dl8 Dl7 Dl8 Dl9 Dl10 Dl1 Dl3 Dl5 Dl7 Dl9 Dl2 Dl4 Dl6 Dl8 Dl10',
'Bl1 Bl2 Dl1 Dl2 Dl3 Dl4 Dl5 Bl1 Bl2 Bl3 Bl4 Dl6 Dl7 Dl8 Dl9 Dl10 Bl3 Bl4 Bl5 Bl6 Bl1 Bl2 Bl5 Bl6 Bl7 Bl8 Bl2 Bl3 Bl7 Bl8 Bl9 Bl10 Bl1 Bl2 Bl3 Bl4 Bl5 Bl6 Bl7 Bl8 Bl9 Bl10 Bl11 Bl12',
'Bl1 Bl2 Bl3 Bl4 Dl1 Dl2 Dl3 Dl4 Dl5 Dl6 Dl7 Dl8 Dl9 Dl10 Bl5 Bl6 Bl7 Bl8 Bl9 Bl10 Bl1 Bl2 Bl3 Bl4 Bl5 Bl6 Bl7 Bl8 Bl9 Bl10 Bl11 Bl12 Bl11 Bl12 Bl13 Bl14 Bl15 Bl16 Dl1 Dl2 Dl3 Dl4 Dl5 Dl6 Dl7 Dl8 Dl9 Dl10 Bl15 Bl16 Bl17 Bl18 Bl19 Bl20 Bl1 Bl2 Bl3 Bl4 Bl5 Bl6 Bl7 Bl8 Bl9 Bl10 Bl11 Bl12 Bl13 Bl14 Bl15 Bl16 Bl17 Bl18 Bl19 Bl20',
'Bl4 Bl5 Bl6 Bl7 Bl8 Bl9 Bl10 Bl11 Bl12 Bl13 Bl14 Bl15 Bl16 Bl17 Bl18 Bl19 Bl20 Xl1 Xl2 Xl3 Xl4 Xl5 Xl6 Xl7 Xl8 Xl9 Xl10 Xl11 Xl12 Xl13 Xl14 Bl1 Bl2 Bl3 Bl4 Bl5 Xl15 Xl16 Xl17 Xl18 Xl1 Xl2 Xl3 Xl4 Xl5 Xl6 Xl7 Xl8 Xl9 Xl10 Xl11 Xl12 Xl13 Xl14 Xl15 Xl16 Xl17 Xl18 Xl19 Xl20 Xl21 Xl22',
'Bl1 Bl2 Dl1 Dl2 Dl3 Dl4 Dl5 Bl1 Bl2 Bl3 Bl4 Dl6 Dl7 Dl8 Dl9 Dl10 Bl3 Bl4 Bl5 Bl6 Bl1 Bl2 Bl5 Bl6 Bl7 Bl8 Bl2 Bl3 Bl7 Bl8 Bl9 Bl10 Bl1 Bl2 Bl3 Bl4 Bl5 Bl6 Bl7 Bl8 Bl9 Bl10 Bl11 Bl12',
'Dl1 Dl2 Dl3 Dl4 Dl5 Dl6 Dl7 Dl8 Dl9 Dl10 Bl1 Bl2 Bl1 Bl2 Bl3 Bl4 Bl3 Bl4 Bl5 Bl6 Bl1 Bl2 Bl5 Bl6 Bl7 Bl8 Bl2 Bl3 Bl7 Bl8 Bl9 Bl10 Bl1 Bl2 Bl3 Bl4 Bl5 Bl6 Bl7 Bl8 Bl9 Bl10 Bl11 Bl12',
'Bl9 Bl10 Bl11 Bl12 Bl1 Bl2 Bl3 Bl4 Bl5 Bl13 Bl14 Bl15 Bl16 Bl6 Bl7 Bl8 Bl9 Bl10 Bl17 Bl18 Bl19 Bl20 Dl1 Dl2 Dl3 Dl4 Dl5 Bl1 Bl2 Bl3 Bl4 Bl5 Bl6 Bl7 Bl8 Bl9 Bl10 Dl6 Dl7 Dl8 Dl9 Dl10 Bl11 Bl12 Bl13 Bl14 Bl15 Bl16 Bl17 Bl18 Bl19 Bl20 Xl1 Xl2 Xl3 Xl4',
'Bl1 Bl2 Bl3 Bl4 Dl6 Dl7 Dl8 Dl9 Dl10 Bl3 Bl4 Bl5 Bl6 Bl1 Bl2 Bl5 Bl6 Bl7 Bl8 Bl2 Bl3 Bl7 Bl8 Bl9 Bl10 Bl1 Bl2 Bl3 Bl4 Bl5 Bl6 Bl7 Bl8 Bl9 Bl10 Bl11 Bl12 Bl13 Bl14 Bl15',
'Bl9 Bl10 Bl11 Bl12 Bl1 Bl2 Bl3 Bl4 Bl5 Bl13 Bl14 Bl15 Bl16 Bl6 Bl7 Bl8 Bl9 Bl10 Bl17 Bl18 Bl19 Bl20 Dl1 Dl2 Dl3 Dl4 Dl5 Bl1 Bl2 Bl3 Bl4 Bl5 Bl6 Bl7 Bl8 Bl9 Bl10 Dl6 Dl7 Dl8 Dl9 Dl10 Bl11 Bl12 Bl13 Bl14 Bl15 Bl16 Bl17 Bl18 Bl19 Bl20 Xl1 Xl2 Xl3 Xl4',
'Bl4 Bl5 Bl6 Bl7 Bl8 Bl9 Bl10 Bl11 Bl12 Bl13 Bl14 Bl15 Bl16 Bl17 Bl18 Bl19 Bl20 Xl1 Xl2 Xl3 Xl4 Xl5 Xl6 Xl7 Xl8 Xl9 Xl10 Xl11 Xl12 Xl13 Xl14 Bl1 Bl2 Bl3 Bl4 Bl5 Xl15 Xl16 Xl17 Xl18 Xl1 Xl2 Xl3 Xl4 Xl5 Xl6 Xl7 Xl8 Xl9 Xl10 Xl11 Xl12 Xl13 Xl14 Xl15 Xl16 Xl17 Xl18 Xl19 Xl20 Xl21 Xl22',
'Bl1 Bl2 Bl3 Bl4 Dl6 Dl7 Dl8 Dl9 Dl10 Bl3 Bl4 Bl5 Bl6 Bl1 Bl2 Bl5 Bl6 Bl7 Bl8 Bl2 Bl3 Bl7 Bl8 Bl9 Bl10 Bl1 Bl2 Bl3 Bl4 Bl5 Bl6 Bl7 Bl8 Bl9 Bl10 Bl11 Bl12 Bl13 Bl14 Bl15',
'Bl9 Bl10 Bl11 Bl12 Bl1 Bl2 Bl3 Bl4 Bl5 Bl13 Bl14 Bl15 Bl16 Bl6 Bl7 Bl8 Bl9 Bl10 Bl17 Bl18 Bl19 Bl20 Dl1 Dl2 Dl3 Dl4 Dl5 Bl1 Bl2 Bl3 Bl4 Bl5 Bl6 Bl7 Bl8 Bl9 Bl10 Dl6 Dl7 Dl8 Dl9 Dl10 Bl11 Bl12 Bl13 Bl14 Bl15 Bl16 Bl17 Bl18 Bl19 Bl20 Xl1 Xl2 Xl3 Xl4',
'Bl1 Bl2 Bl3 Bl4 Dl6 Dl7 Dl8 Dl9 Dl10 Bl3 Bl4 Bl5 Bl6 Bl1 Bl2 Bl5 Bl6 Bl7 Bl8 Bl2 Bl3 Bl7 Bl8 Bl9 Bl10 Bl1 Bl2 Bl3 Bl4 Bl5 Bl6 Bl7 Bl8 Bl9 Bl10 Bl11 Bl12 Bl13 Bl14 Bl15',
'Bl1 Bl2 Bl3 Bl4 Dl6 Dl7 Dl8 Dl9 Dl10 Bl3 Bl4 Bl5 Bl6 Bl1 Bl2 Bl5 Bl6 Bl7 Bl8 Bl2 Bl3 Bl7 Bl8 Bl9 Bl10 Bl1 Bl2 Bl3 Bl4 Bl5 Bl6 Bl7 Bl8 Bl9 Bl10 Bl11 Bl12 Bl13 Bl14 Bl15',
			]
print len(lisnum_gs)

lisnum_gs = map(splitter,lisnum_gs)

#generator(name_gs,groups,lisnum_gs,originalData, subdirectory =output_dir)
print_tel(name_gs)
