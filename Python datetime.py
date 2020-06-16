import time
import datetime
from datetime import datetime

# https://www.w3resource.com/python-exercises/date-time-exercise/index.php
# 1. Write a Python script to display the various Date Time formats
# a) Current date and time
datetime.today()
now = datetime.now()
# b) Current year
now.year
now.strftime("%Y")
# c) Month of year
now.month
now.strftime("%B")
# d) Week number of the year
now.strftime("%W")
# e) Weekday of the week
now.strftime("%A")
# f) Day of year
now.strftime("%j")
# g) Day of the month
now.strftime("%d")
# h) Day of week
now.strftime("%A")

# 2. Write a Python program to determine whether a given year is a leap year.
year = input(datetime.year)
my_string = year + "-12-31"
my_date = datetime.strptime(my_string, "%Y-%m-%d")
days_of_the_year = my_date.strftime("%j")

if days_of_the_year == '366':
    print("Leap year")
else:
    print("not a leap year")

# 3. Write a Python program to convert a string to datetime.
# Sample String : Jan 1 2014 2:43PM
# Expected Output : 2014-07-01 14:43:00
sample = datetime.strptime("Jan 1 2014 2:43PM", '%b %d %Y %I:%M%p')
sample.strftime("%Y-%m-%d %H:%M:%S")
# 4. Write a Python program to get the current time in Python
# now.strftime("%H:%M:%S")

import datetime
#5. Write a Python program to subtract five days from current date. Go to the editor
#Sample Date :
#Current Date : 2015-06-22

tdelta=datetime.timedelta(days=+5)
current_date=datetime.datetime.strptime("2015-6-22", "%Y-%m-%d")
sample_date=current_date+tdelta
sample_date.strftime("%Y%m%d")

#6. Write a Python program to convert unix timestamp string to readable date. Go to the editor
#Sample Unix timestamp string : 1284105682
#Expected Output : 2010-09-10 13:31:22

#7. Write a Python program to print yesterday, today, tomorrow.
today=datetime.datetime.today()
tdelta=datetime.timedelta(days=+1)
tomorrow=today+tdelta
tomorrow.strftime("%Y-%m-%d")

day_before_delta=datetime.timedelta(days=-1)
yesterday=today+day_before_delta
yesterday.strftime('%Y-%m-%d')

#strftime: string from time
#strptime: string parse time
#"parse" in Wiktionary is "To split a file or other input into pieces of data that can be easily stored or manipulated.

#8. Write a Python program to convert the date to datetime (midnight of the date) in Python. Go to the editor
#Sample Output : 2015-06-22 00:00:00

today=datetime.date.today()
datetime.datetime.combine(today,datetime.datetime.min.time())

#9. Write a Python program to print next 5 days starting from today. Go to the editor
today=datetime.date.today()
today
five_day_delta=datetime.timedelta(days=+5)
today+five_day_delta

# 10. Write a Python program to add 5 seconds with the current time. Go to the editor
now=datetime.datetime.now()
five_second_delta=datetime.timedelta(seconds=+5)
now+five_second_delta

# 11. Write a Python program to convert Year/Month/Day to Day of Year in Python.
today=datetime.datetime.today()
last_day=datetime.datetime.strptime('2019-12-31',"%Y-%m-%d")
(today-last_day).days

#or
(today-datetime.datetime(today.year,1,1)).days+1

#12. Write a Python program to get current time in milliseconds in Python
datetime.datetime.now()
#or
import time
time.time()*1000

#13. Write a Python program to get week number. Go to the editor
#Sample Date : 2015, 6, 16
#Expected Output : 25
sample = datetime.datetime.strptime ("Jan 1 2014 2:43PM", '%b %d %Y %I:%M%p')
import datetime
sample=datetime.date(2015,6,15)
sample.isocalendar()[1]

#https://www.w3resource.com/python-exercises/pandas/datetime/index.php
import pandas as pd
df=pd.read_csv('http://bit.ly/uforeports', index_col='Time', parse_dates=True)
df.index

#Pandas datetime
#https://www.w3resource.com/python-exercises/pandas/datetime/index.php
# 1. Write a Pandas program to create the todays date.
import datetime
datetime.date.today()
now = datetime.datetime.now()
now
#2. Write a Pandas program to calculate all the sighting days of the unidentified flying object (ufo) from current date.
df.index.date

#3. Write a Pandas program to get the current date, oldest date and number of days between Current date and oldest date of Ufo dataset.
latest=old=df.sort_index().index[-1]
old=df.sort_index().index[0]
(latest-old).days

#or
(df.index.max()-df.index.min()).days

#4. Write a Pandas program to get all the sighting days of the unidentified flying object (ufo) which are less than or equal to 40 years (365*40 days).
duration=datetime.timedelta(days=-365*40)
cutoff=pd.to_datetime('today')+duration
df[df.index>=cutoff]

#5. Write a Pandas program to get all the sighting days of the unidentified flying object (ufo) between 1950-10-10 and 1960-10-10
start=datetime.datetime.strptime('1950-10-10','%Y-%m-%d')
end=datetime.date(1960,10,10)
df[(df.index>pd.to_datetime(start))&(df.index<pd.to_datetime(end))] #remember df[()&()]format

#6. Write a Pandas program to get all the sighting years of the unidentified flying object (ufo) and create the year as column
df.index.year
#or
df['Date_time']=df.index
df['year']=df.Date_time.dt.year

#7. Write a Pandas program to create a plot to present the number of unidentified flying object (UFO) reports per year.
#year=df.year.value_counts().sort_value() this gives sort by values
year=df.year.value_counts().sort_index()

#8. Write a Pandas program to extract year, month, day, hour, minute, second and weekday from unidentified flying object (UFO) reporting date.
df.index.year
df['month']=df.index.month
df['day']=df.index.day
df['hour']=df.index.hour
df['minute']=df.index.minute
df['second']=df.index.second
df['weekday']=df.index.weekday
#another methodology
df.Date_time.dt.year
df.Date_time.dt.month

#9. Write a Pandas program to convert given datetime to timestamp.
#10. Write a Pandas program to count year-country wise frequency of reporting dates of unidentified flying object(UFO).
df.head()
df.groupby(['year','City']).size()

#11. Write a Pandas program to extract unique reporting dates of unidentified flying object (UFO).
df.index.date
df['Date_time'].map(lambda t:t.date()).unique()
df['Date_time'].map(lambda t:t.date())


# 11. Write a Pandas program to extract unique reporting dates of unidentified flying object (UFO)
df.index=pd.to_datetime(df.index)
df.index
df.index.date

df

#12. Write a Pandas program to get the difference (in days) between documented date and reporting date of unidentified flying object (UFO).

df['days_difference']=(df.Date_time-df.index).dt.days
df

#13. Write a Pandas program to add 100 days with reporting date of unidentified flying object (UFO).
d_delta=datetime.timedelta(days=+100)
df['+100days']=df.index+d_delta
df

#14. Write a Pandas program to generate sequences of fixed-frequency dates and time spans.
pd.date_range('2018-01-01',periods=12,freq='H')

#15. Write a Pandas program to create a conversion between strings and datetime.
df.dtypes
df['date']=df.index.astype('int')
df.dtypes
df['date']=pd.to_datetime(df.date)

#16. Write a Pandas program to manipulate and convert date times with timezone information.

#17. Write a Pandas program to get the average mean of the UFO (unidentified flying object) sighting was reported.
df.index.year.value_counts().sort_index()
#18. Write a Pandas program to create a graphical analysis of UFO (unidentified flying object) Sightings year.
import matplotlib.pyplot
df.index.year.value_counts().sort_index().plot()
#19. Write a Pandas program to check the empty values of UFO (unidentified flying object) Dataframe.
df.isnull().sum()