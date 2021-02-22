import datetime
import pandas as pd
import pytz

time_now=datetime.datetime.now()
print(time_now)

# startdate=datetime.datetime(2021,6,30,4,30,59)
# t=startdate.strftime("%Y/%m/%d:%H:%M:%S")
# print(t)

# print(startdate)

# date_1="31 January 2021"
# date_object=datetime.datetime.strptime(date_1,"%d %B %Y")
# print(date_object)

tz_la=pytz.timezone("Europe/London")
datetime_york=datetime.datetime.now(tz_la)
print(datetime_york)