from datetime import datetime, timedelta

def parse(line):
    d, t, tz = line.split()
    dt = datetime.strptime(d + " " + t, "%Y-%m-%d %H:%M:%S")
    sign = 1 if tz[3] == '+' else -1
    h, m = map(int, tz[4:].split(":"))
    return dt - timedelta(hours=h, minutes=m)*sign

start = parse(input().strip())
end = parse(input().strip())

print(int((end - start).total_seconds()))