import sys

num = int(sys.stdin.readline())

# 1 / 2 ~ 7 / 8 ~ 19 / 20 ~ 37 / 38 ~ 61
line = 1
lineMaxnum = 1
while(num > lineMaxnum):
    lineMaxnum = (line - 1) * 6 + lineMaxnum
    line += 1

if (line == 1):
    print(line)
else:
    print(line - 1)
