# import module
import calendar
   
yy = 2017
mm = 11
   
# display the calendar
print(calendar.month(yy, mm))

print ("The calendar of year 2018 is : ")
print (calendar.calendar(2018))

# Operations on the calendar : 
# 1. calendar(year, w, l, c):- This function displays the year, the width of characters, no. of lines per week, and column separations.
# 2. firstweekday() :- This function returns the first week day number. By default 0 (Monday).

print ("The calendar of year 2012 is : ")
print (calendar.calendar(2012,2,1,6))
 
#using firstweekday() to print starting day number
print ("The starting day number in calendar is : ",end="")
print (calendar.firstweekday())

# using isleap() to check if year is leap or not
if (calendar.isleap(2008)):
       print ("The year is leap")
else : print ("The year is not leap")
 
#using leapdays() to print leap days between years
print ("The leap days between 1950 and 2000 are : ",end="")
print (calendar.leapdays(1950, 2000))

# 5. month (year, month, w, l) :- This function prints the month of a specific year mentioned in arguments. It takes 4 arguments, year, month, width of characters and no. of lines taken by a week.

# using month() to display month of specific year
print ("The month 5th of 2016 is :")
print (calendar.month(2016,5,2,1))

# Program to display calendar of the given month and year

# importing calendar module
import calendar

yy = 2014  # year
mm = 11    # month

# To take month and year input from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))

c= calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(2025,1)
print(str)

hc = calendar.HTMLCalendar(calendar.THURSDAY)
str = hc.formatmonth(2025,1)
print(str)

for day in calendar.day_name:
    print(day)