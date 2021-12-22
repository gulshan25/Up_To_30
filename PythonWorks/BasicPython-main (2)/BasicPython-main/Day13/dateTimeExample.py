# Date and time
# Python has a module named datetime 
# to work with dates and times

# from datetime import datetime, date 
# Commonly used classes in the datetime 
# module are:

# 	date Class
# 	time Class
# 	datetime Class
# 	timedelta Class


#Get current date and time
import datetime
datetime_obj = datetime.datetime.now()
print(datetime_obj)

datetime_obj = datetime.date.today()
print(datetime_obj)

from datetime import datetime,date

cdate = datetime.now()
print(cdate)

cdate1 = date.today()
print(cdate1)

print(cdate.year)
print(cdate.month)
print(cdate.day)

print(cdate.hour)
print(cdate.minute)
print(cdate.second)
print(cdate.microsecond)

print(cdate.strftime('Weekday Short : %a'))
print(cdate.strftime('Weekday Long : %A'))
print(cdate.strftime('Weekday Number : %w'))

print(cdate.strftime('Month Short : %b'))
print(cdate.strftime('Month Long : %B'))
print(cdate.strftime('Month Number : %m'))

print(cdate.strftime('Day of Month : %d'))
print(cdate.strftime('Year without centuary : %y'))
print(cdate.strftime('Year with    centuary : %Y'))

print(cdate.strftime('Full Time 0-23 : %T'))
print(cdate.strftime('Full Date      : %D'))

print(cdate.strftime('Hour 0-23      : %H'))
print(cdate.strftime('Hour 0-12      : %I'))
print(cdate.strftime('am/pm          : %p'))
print(cdate.strftime('Minute         : %M'))
print(cdate.strftime('Second         : %S'))
print(cdate.strftime('MicroSecond    : %f'))

print('Display custom format')
print('-'*40)

print(cdate.strftime('%d-%m-%Y'))
print(cdate.strftime('%A, %m-%d-%Y'))
print(cdate.strftime('%Y/%m/%d'))

print(cdate.strftime('%I:%M:%S %p'))
print(cdate.strftime('%H:%M:%S'))

from datetime import datetime,date

t1 = date(year=2018,month=7, day=12)
t2 = date(year=2017,month=12, day=23)
t3= t1-t2
print('t3 = ',t3)

t4 = datetime(year=2018, month=7,day=12, hour=7, minute=9,second=33)
t5 = datetime(year=2017, month=12,day=23, hour=5, minute=55,second=13)

t6 = t4-t5
print('t6 = ',t6)