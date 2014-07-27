import fileinput,re

field_pat = re.compile(r'\[(.+)\]')

scope = {}

def replacement(match):
	code = match.group(1)
	try:
		return str(eval(code,scope))
	except SyntaxError:
		exec code in scope
		return ''


file = open('template')
text=''.join(file.readlines())

print field_pat.sub(replacement,text)