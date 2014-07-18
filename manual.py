import collector
from collector import print_dict
#print collector.__doc__
#intial data need to be initialized 
filename = '/Users/Zhe/Desktop/sat_july_2014/data/data_2014.07.17/output1'

originalData = collector.data(filename)
#print originalData


from datetime import date
em = date.today()
curdate = '%s.%s.%s'%(em.year,em.month,em.day)
print curdate

inputfile = '/Users/Zhe/Desktop/sat_july_2014/data/data_2014.07.17/group02014.7.17 2.txt'
outputfile = '/Users/Zhe/Desktop/sat_july_2014/data/data_2014.07.17/output1'

def update_data(inputfile,outputfile,parser):#parser should be imported from collector
	Parser = parser(inputfile)
	f = Parser.parser()
	originalData.update(f,output = outputfile)
	print originalData
parser = collector.vocab_parser #, collector.basic_parser collector.CRmock_parser
print_dict(originalData.get_student('RuolinMeng')['Tel']) 
#update_data(inputfile,outputfile,parser)
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


# import word_processor
# #print word_processor.__doc__
# generator = word_processor.generate_list_specific
# output_dir = '/Users/Zhe/Desktop/sat_july_2014/data/data_2014.07.18'

# # # name_gs =['sb','notsb1','notsb2']
# # # groups = [['ZhangJianxin', 'GuoZiwei', 'ZhouMingrui', 'ChenYanghui', 'GaoYueMing', 'HuKangrui', 'LiuHuijun', 'ZhangShenghong'],
# # # 			['LiZhijian', 'ZhangXiaoying', 'ShiQianyi', 'ZhuoJiaming', 'ChenAnran', 'LiRuxian'],
# # # 			['GaoYichen', 'HuangYiheng', 'LiXingrong', 'WuShiqi', 'Mengruolin', 'XieChen']]
# # # lisnum_gs = [['Dl5','Dl6','Dl8','Dl9'],['Dl5','Dl6','Dl8','Dl9'],['Dl5','Dl6','Dl8','Dl9']]
# name_gs = ['group0','group1']
# groups = [['JianxinZhang', 'ZiweiGuo', 'MingruiZhou', 'YuemingGao'],['AnranChen','RuolinMeng']]
# lisnum_gs =[['Dl1','Dl2','Dl3','Dl4'],['Dl1','Dl2','Dl3','Dl4']]



#generator(name_gs,groups,lisnum_gs,originalData, subdirectory =output_dir)
