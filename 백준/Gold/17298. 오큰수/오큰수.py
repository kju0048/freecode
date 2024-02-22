# 17298
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
lista = list(map(int, input().split()))
ans = [0] * N

mstack = []
for i in range(N):
    while mstack and lista[mstack[-1]] < lista[i]:
        ans[mstack.pop()] = lista[i]
    mstack.append(i)


while mstack:
    ans[mstack.pop()] = -1
    
for i in range(N):
    print(str(ans[i]), end= " ")