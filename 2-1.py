#!/usr/bin
# coding=utf-8
months=[
	'Januay',
	'February',
	'March',
	'April',
	'May',
	'June',
	'July',
	'Auguest',
	'September',
	'October',
	'November',
	'December'
]
# һ���б����а�����1~31��Ӧ�Ľ�β
endings=['st','nd','rd']+17*['th']+['st','nd','rd']+7*['th']+['st']

year=input('Year:')
month=input('Month(1-12):')
day=input('Day(1-31):')
month_number=int(month)
day_number=int(day)
#��ʾ�����յ��������б���Ҫ��ȥһ
month_name=months[month_number-1]
ordinal=day+endings[day_number-1]
print(month_name+' '+ordinal+' '+year)
input('Please Enter end')