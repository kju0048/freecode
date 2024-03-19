# 18110
import sys

input = sys.stdin.readline

n = int(input())
cut = int((n * 15 / 100) + 0.5)
lists = []

for i in range(n):
    lists.append(int(input()))
    
if n == 0:
    print(0)
else: 
    lists.sort()
    cutlist = lists[cut : n-cut]

    print(int((sum(cutlist)/len(cutlist))+0.5))