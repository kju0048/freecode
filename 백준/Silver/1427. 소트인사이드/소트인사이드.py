# 1427
import sys

input = sys.stdin.readline

n = str(input())

listn = [int(x) for x in n.strip('\n')]
len_n = len(listn)

for x in range(len_n):
    max = 0
    idx = -1
    for y in range(x, len_n):
        if max < listn[y]:
            max = listn[y]
            idx = y
    if idx != -1:
        listn[x], listn[idx] = listn[idx], listn[x]
    print(listn[x], end='')