import sys

num = int(sys.stdin.readline())

line = 1
while(num > line):
    num -= line
    line += 1

if line%2 == 0:
    a = num
    b = line - num + 1
else:
    a = line - num + 1
    b = num

print(a, b, sep="/")