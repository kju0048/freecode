# 10986
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lista = list(map(int, input().split()))
listb = []
sum = 0
perCount = [0 for x in range(m)]

for i in lista:
    sum += i
    perCount[sum%m] += 1
    listb.append(sum%m)

res = 0

for i in perCount:
    res += i * (i-1) // 2
res += perCount[0]

print(res)