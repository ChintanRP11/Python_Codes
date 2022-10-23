import datetime

print(datetime.MAXYEAR)
print(datetime.MINYEAR)

now = datetime.datetime.today()
other = datetime.datetime(1999,7,5,00,11,34,456456)
print(datetime.datetime(1999,12,17,22,34,34,456456))
# it is year, month, day, hours, minute, sec, msec
print(now)
print(now - other)