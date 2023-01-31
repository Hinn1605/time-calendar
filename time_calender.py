import calendar
import time

year=int(input("Nam: "))
month=int(input("Thang: "))

t=time.localtime(time.time())
localtime=time.asctime(t)
str=time.asctime(t)

print(calendar.month(year, month))
print(str)