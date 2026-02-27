# A date in Python is not a data type of its own, but we can import a module named ! datetime ! to work with dates as date objects.
#ex
import datetime

x = datetime.datetime.now()
print(x)                    #2026-02-27 19:33:55.557198 (current time)

#ex
import datetime

x = datetime.datetime.now()
print(x.year)                #2026
print(x.strftime("%A"))      #Friday

'''strftime() function lets us convert a datetime object into a formatted string using special format codes. 
%Y gives the full year, %m gives the month, %d gives the day.
%H:%M:%S returns the hour, minute, and second in 24-hour time format.
%p: Locale's equivalent of AM or PM.
%I: Hour in 12-hour clock (01–12) — usually used with %p.
%H: Hour in 24-hour clock (00–23). '''

#ex (To create a date)
import datetime

x = datetime.datetime(2020, 5, 17)
print(x)                           #2020-05-17 00:00:00

#ex
import datetime

x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))           #June
