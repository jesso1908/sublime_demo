import datetime

datetime_object = datetime.datetime.now()
print(datetime_object)

date_object = datetime.date.today()
print(date_object)


d = datetime.date(2019, 4, 13)
print(d)

timestamp = datetime.date.fromtimestamp(1326244364)
print("Date =", timestamp)

from datetime import date

# date object of today's date
today = date.today() 

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)