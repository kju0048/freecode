import sys

h, m, s = map(int, sys.stdin.readline().split())
tt = int(sys.stdin.readline())

sett = s + (60 * m) + (3600 * h) + tt
if sett >= 86400:
    sett %= 86400

h = sett // 3600
m = (sett % 3600) // 60
s = sett % 60
print("{} {} {}".format(h, m, s))