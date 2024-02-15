import sys
from math import floor, ceil
input = sys.stdin.readline

n = int(input())
m = int(input())
lista = list(map(int, input().split()))

list_sort = sorted(lista)
p1 = 0
p2 = n - 1
count = 0

while p1 < p2:
    if list_sort[p1] + list_sort[p2]  == m:
        count += 1
        p1 += 1
        p2 -= 1
    elif list_sort[p1] + list_sort[p2] > m:
        p2 -= 1
    else:
        p1 += 1
        
print(count)