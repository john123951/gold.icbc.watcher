import time
import datetime

now = datetime.datetime.now()
print(now)

d2 = datetime.datetime(2016, 11, 15)
print(d2)

span = now - d2
print(span.seconds)
