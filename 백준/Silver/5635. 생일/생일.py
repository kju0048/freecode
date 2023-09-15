import sys
import datetime
inp = sys.stdin.readline

n = int(inp())
dictDate = {}
max = datetime.date(2010, 12, 31)
min = datetime.date(1990, 1, 1)

for i in range(n):
    name, d, m, y = map(str, inp().split())
    dictDate[name] = datetime.date(int(y), int(m) ,int(d))
    if min < dictDate[name]:
        min = dictDate[name]
        minName = name
    if max > dictDate[name]:
        max = dictDate[name]
        maxName = name

print(minName)
print(maxName)