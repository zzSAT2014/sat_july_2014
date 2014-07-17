import collector
#print collector.__doc__
#intial data need to be initialized 
filename = '/Users/Zhe/Desktop/sat_july_2014/data/data_2014.07.15/test'
originalData = collector.data(filename)
#print originalData


from datetime import date
em = date.today()
curdate = '%s.%s.%s'%(em.year,em.month,em.day)



outputfile = '/Users/Zhe/Desktop/sat_july_2014/test'



#vocab update
# vocab_parser_filename = ''
# vocabParser = collector.vocab_parser(vocab_parser_filename)
# vocab_parser = vocabParser.parser()
# originalData.update(vocab_parser,output = outputFile)

# basic information update
# basic_parser_filename = ''
# basicParser = collector.basic_parser(basic_parser_filename)
# basic_parser = basicParser.parser()
# originalData.update(basic_parser,output = outputFile)



import word_processor
#print word_processor.__doc__
generator = word_processor.generate_list_specific
output_dir = '/Users/Zhe/Desktop/testing'

# name_gs =['sb','notsb1','notsb2']
# groups = [['ZhangJianxin', 'GuoZiwei', 'ZhouMingrui', 'ChenYanghui', 'GaoYueMing', 'HuKangrui', 'LiuHuijun', 'ZhangShenghong'],
# 			['LiZhijian', 'ZhangXiaoying', 'ShiQianyi', 'ZhuoJiaming', 'ChenAnran', 'LiRuxian'],
# 			['GaoYichen', 'HuangYiheng', 'LiXingrong', 'WuShiqi', 'Mengruolin', 'XieChen']]
# lisnum_gs = [['Dl5','Dl6','Dl8','Dl9'],['Dl5','Dl6','Dl8','Dl9'],['Dl5','Dl6','Dl8','Dl9']]
name_gs = ['group0']
groups = [['KangruiHu,YuemingGao,ZiweiGuo,MingruiZhou,YueChen,HuijunLiu']]
lisnum_gs =[['Dl1','Dl2']]
generator(name_gs,groups,lisnum_gs,originalData, subdirectory =output_dir)