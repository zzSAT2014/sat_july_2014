import collector
from collector import print_dict
#print collector.__doc__
#intial data need to be initialized 
filename = '/Users/Zhe/Desktop/sat_july_2014/data/newmaster'

originalData = collector.data(filename,mode = 'db')
# print originalData
#print_dict(originalData)

from datetime import date
em = date.today()
curdate = '%s.%s.%s'%(em.year,em.month,em.day)
print curdate

inputfile = '/Users/Zhe/Desktop/sat_july_2014/data/danci/kaoshi'

outputfile = '/Users/Zhe/Desktop/sat_july_2014/data/database2'

def update_data(inputfile,outputfile,parser):#parser should be imported from collector
	Parser = parser(inputfile)
	f = Parser.parser()
	originalData.update(f)#output = outputfile)
	#print originalData
parser = collector.cr_practice_parser
originalData.update(lambda x:x, output = outputfile)
print_dict(originalData.get_student('RuolinMeng'))
# collector.CRmock_parser#collector.vocab_parser #, collector.basic_parser collector.CRmock_parser, #vocab_parser
# update_data(inputfile,outputfile,parser)
#print_dict(originalData.get_student(''))
#print originalData.get_student('JiamingZhuo')['Tel']
# print_dict(originalData.get_student('ZhijianLi'))



print_dict(originalData.get_student('scoregroup')) 

def print_tel(lis):
	for name in lis:
		print name + '\tTel\t:' + repr(originalData.get_student(name)['Tel'])

lis= ['RuxianLi','ChenXie','ShiqiWu']



import word_processor
# #print word_processor.__doc__
generator = word_processor.generate_list_specific
output_dir = '/Users/Zhe/Desktop/sat_july_2014/data/data_2014.08.04'

# names =['YuemingGao', 'ShiqiWu', 'MingruiZhou', 'RuolinMeng', 'ChenXie', 'AnranChen', 'QianyiShi', 'ZhijianLi', 'XinrongLi', 'RuxianLi']
# lists = ['Bl11 Bl12 Bl13 Bl14 Dl1 Dl2 Dl3 Dl4 Dl5 Bl13 Bl14 Bl15 Bl16 Dl6 Dl7 Dl8 Dl9 Dl10', 'Xl1 Xl2 Xl3 Xl4 Xl5 Xl6 Xl7 Xl8 Xl9 Xl10 Xl11 Xl12 Xl13 Xl14 Bl1 Bl2 Bl3 Bl4 Bl5', 'Bl1 Bl2 Bl5 Bl6 Bl7 Bl8 Bl2 Bl3 Bl7 Bl8 Bl9 Bl10 Bl1 Bl2 Bl3 Bl4 Bl5', 'Xl1 Xl2 Xl3 Xl4 Xl5 Xl6 Xl7 Xl8 Xl9 Xl10 Xl11 Xl12 Xl13 Xl14 Bl1 Bl2 Bl3 Bl4 Bl5', 'Bl11 Bl12 Bl13 Bl14 Dl1 Dl2 Dl3 Dl4 Dl5 Bl13 Bl14 Bl15 Bl16 Dl6 Dl7 Dl8 Dl9 Dl10 Bl15 Bl16 Bl17 Bl18', 'Xl5 Xl6 Xl7 Xl8 Xl9 Xl10 Xl11 Xl12 Xl13 Xl14 Bl1 Bl2 Bl3 Bl4 Bl5 Xl15 Xl16 Xl17 Xl18 Xl1 Xl2 Xl3 Xl4 Xl5 Xl6 Xl7 Xl8 Xl9 Xl10', 'Xl25 Xl26 Xl27 Xl28 Xl29 Xl30 Xl31 Xl32 Xl33 Xl34', 'Xl25 Xl26 Xl27 Xl28 Xl29 Xl30 Xl31 Xl32 Xl33 Xl34', 'Bl11 Bl12 Bl13 Bl14 Dl1 Dl2 Dl3 Dl4 Dl5 Bl13 Bl14 Bl15 Bl16 Dl6 Dl7 Dl8 Dl9 Dl10 Bl15 Bl16 Bl17 Bl18', 'Bl11 Bl12 Bl13 Bl14 Dl1 Dl2 Dl3 Dl4 Dl5 Bl13 Bl14 Bl15 Bl16 Dl6 Dl7 Dl8 Dl9 Dl10 Bl15 Bl16 Bl17 Bl18']
# name_gs =
# groups = [['QianyiShi']]
# lisnum_gs = [['Bl7','Bl8','Dl9','Dl10']]
# splitter = lambda string: string.split()
# lists = map(splitter, lists)
# change_to_list = lambda x: [x,]
# groups = map(change_to_list,names)
# lis = ['AnranChen','ChenXie','HaoranLiao','MingruiZhou','QianyiShi','RuolinMeng','RuxianLi','ShiqiWu','XiaoyingZhang','XinrongLi','YuemingGao','ZhijianLi']
# groups =  lis
# convert = lambda a: [a]
# groups = map(convert,groups)
# line = 0
# for student in lis:
# 	line+=1
# 	print str(line)+'\t',
# 	print student + '\t\t\t',
# 	print originalData.get_student(student)['SAT']['FirstTest']


# #lisnum_gs = map(splitter,lisnum_gs)

# generator(names,groups,lists,originalData, subdirectory =output_dir)
# print_tel(name_gs)
