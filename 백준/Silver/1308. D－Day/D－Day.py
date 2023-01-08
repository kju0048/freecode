import sys
from datetime import datetime, timedelta
inp = sys.stdin.readline

today = list(map(int, inp().split()))
dday = list(map(int, inp().split()))

today = datetime(today[0], today[1], today[2])
dday = datetime(dday[0], dday[1], dday[2])

if dday.year - today.year > 1000 or (dday.year - today.year == 1000 and today.month < dday.month) \
    or (dday.year - today.year == 1000 and today.month == dday.month and today.day <= dday.day):
    print("gg")
else:
    print("D-" + str((dday - today).days))