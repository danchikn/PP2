import datetime
a = datetime.datetime.now()
b = datetime.datetime(2023,2,19,22,28,30)
c = a - b
seconds = c.total_seconds()
print(seconds)