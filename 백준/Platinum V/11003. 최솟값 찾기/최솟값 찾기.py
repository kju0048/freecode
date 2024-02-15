# 11003
import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())
lista = list(map(int, input().split()))
deque_a = deque()


for i in range(N):
    while deque_a and deque_a[-1][0] > lista[i]:
        deque_a.pop()
    deque_a.append((lista[i], i))

    if deque_a[0][1] <= i - L:
        deque_a.popleft()
    print(deque_a[0][0], end=' ')