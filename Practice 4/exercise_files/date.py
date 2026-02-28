#ex1
from datetime import datetime, timedelta

now = datetime.now()
5_days_ago = now - timedelta(days=5)
print(5_days_ago)


#ex2
from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)


#ex3
from datetime import datetime

now = datetime.now()
no_micro = now.replace(microsecond=0) #removes microseconds from the datetime object.
print(no_micro)


#ex4
from datetime import datetime

date1 = datetime(2026, 1, 1, 0, 0, 0)   #or date1 = datetime.strptime(d1, "%Y-%m-%d %H:%M:%S")
date2 = datetime(2026, 1, 2, 1, 30, 0)

diff = date2 - date1
seconds = diff.total_seconds()
print(int(seconds))
