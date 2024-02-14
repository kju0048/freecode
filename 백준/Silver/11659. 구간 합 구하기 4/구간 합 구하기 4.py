# 11659 
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lista = list(map(int, input().split()))
listsum = [0]
sum = 0
for i in lista:
    sum += i
    listsum.append(sum)

for i in range(m):
    a, b = map(int, input().split())
    print(listsum[b] - listsum[a-1])