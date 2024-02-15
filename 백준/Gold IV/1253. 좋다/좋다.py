# 1253
import sys
from math import floor, ceil
input = sys.stdin.readline

n = int(input())
lista = list(map(int, input().split()))

list_sort = sorted(lista)
count = 0

for i in range(n):
    p1 = 0
    p2 = n-1
    while p1 < p2:
        if list_sort[p1] + list_sort[p2] == list_sort[i]:
            if p1 != i and p2 != i:
                count += 1
                break
            elif p1 == i:
                p1 += 1
            elif p2 == i:
                p2 -= 1
        elif list_sort[p1] + list_sort[p2] > list_sort[i]:
            p2 -= 1
        else:
            p1 += 1
print(count)