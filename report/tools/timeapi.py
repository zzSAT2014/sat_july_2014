import sys
#access to current level files
import os


from datetime import date
from datetime import timedelta

#print date.today()
def timeapi_to_date(api):
	'''api <--- a string like 2014.08.15

	 date---> datetime.date object'''
	api = api.split('.')
	api = map(int, api)
	return date(*api)

def date_to_api(date):
	'''input date<---datetime.date object

		output ---> date in api format i.e. 2014.08.15'''
	return '%s.%s.%s'%(date.year,date.month,date.day)


def dates_before(delta, curdate = None):
	'''Input: 
		delta <---int,  number of dates from current date
		curdate <--- start point as 
	Output:
		past ---> all relevant dates counting from today, i.e. 1 == [yesterday,]'''
	print date.today()
	if not curdate: today = date.today()
	else: today = timeapi_to_date(curdate)
	past= []
	diff = 0
	
	while diff < delta:
		diff += 1
		d = timedelta(-diff)

		pastdate = date_to_api(today + d)
		past.append(pastdate)
	return past

def test_dates_before():
	print dates_before(5)
systoday = date_to_api(date.today())
#print sys_today
#test_dates_before()