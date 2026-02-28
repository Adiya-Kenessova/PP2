from datetime import datetime, timedelta

l1 = input()
l2 = input()

def get_utc(a):
    parts = a.split()

    date = parts[0]
    tz = parts[1]

    date = datetime.strptime(date, "%Y-%m-%d") #string → parse → time

    if tz[3] == '+':
        sign = 1
    else:
        sign = -1

    h,m = map(int, tz[4:].split(':'))
    offset = timedelta(hours=h, minutes=m)
    utc_time = date - sign * offset     #The input date is local midnight.

    return utc_time

time1 =  get_utc(l1)
time2 = get_utc(l2)

seconds = abs((time1 - time2).total_seconds())
days = int(seconds // 86400)

print(days)


