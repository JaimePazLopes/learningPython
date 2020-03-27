import datetime

time = datetime.time(5, 25, 1)
print(time)
print(datetime.time.min)
print(datetime.time.max)
print(datetime.time.resolution)

today = datetime.date.today()
print(today)
print(today.timetuple())
print(today.day)
date1 = datetime.date(2000, 1, 1)
print(date1)
date2 = date1.replace(year = 2020)
print(date2)
print(date2 - date1)




