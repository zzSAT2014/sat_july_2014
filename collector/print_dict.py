
def print_dict(dic):
	'''this module prints dictionary for visualization


	input  --> dictionay
	output  --> None'''


	separator = '-->'
	indentation = '    '
	#@trace
	def inner(dic,inlevel=0):
		if type(dic) is not dict: print indentation*inlevel+repr(dic)
		else:
			for key in dic:
				print indentation*inlevel + repr(key) + separator
				
				inner(dic[key],inlevel+1)
	inner(dic)

