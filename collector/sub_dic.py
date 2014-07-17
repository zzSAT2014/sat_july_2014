from copy import copy


def csub_dict(dic,lis,value):
	'''create a subdictionary if there there is not one'''
	#print '\t\tvalue in c_sub\t%s'%value
	if len(lis) == 0:
		return value
	else:
		dic[lis[0]] = {} 
		dic[lis[0]] = csub_dict(dic[lis[0]],lis[1:],value)
		#print '\t\tindide c_sub \t %s'%(dic)
		return dic
#@trace
def sub_dict(dic,lis,func=lambda x:x,value=None,copy=None):
	'''dic target dicttionary
		lis --> target directory
		mutate the bottom value using func'''
	#print lis
	#print '\tvalue in sub\t%s' %(value)
	if lis[0] not in dic: 
		#print 'creat'

		csub_dict(dic,lis,value)
		#print 'inside sub_dic%s\t'%(dic)
	#print dic
	if len(lis) == 1:
		dic[lis[0]] = func(dic[lis[0]])
	else: sub_dict(dic[lis[0]],lis[1:],func,value)

def sub_test():
	a = {1:{2:{3:'b'}},2:{3:4,5:6}}
	f = lambda x: 1
	b=sub_dict(a,[1,2,3],func = f,value='a')
	b = sub_dict(a,[2,3],func=f)
	b = sub_dict(a,[3,4])
	print a
#sub_test()