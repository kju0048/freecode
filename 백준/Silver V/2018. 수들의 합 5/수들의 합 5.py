# 2018
import sys
from math import floor, ceil
input = sys.stdin.readline

n = int(input())
p1 = floor(n/2)
p2 = ceil(n/2)
count = 0

while p1 > 0:
    if (p1 + p2) * (p2 - p1 + 1) / 2  == n:
        count += 1
        p1 -= 1
    elif (p1 + p2) * (p2 - p1 + 1) / 2  > n:
        p2 -= 1
    else:
        p1 -= 1
        
print(count + 1)