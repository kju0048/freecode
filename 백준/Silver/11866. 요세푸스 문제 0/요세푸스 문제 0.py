import sys
from collections import deque

inp = sys.stdin.readline

n, k = map(int, inp().split())

list = deque([x for x in range(1, n+1)])

list.rotate(-k + 1)
print("<{}".format(list.popleft()), end="")
for i in range(n-1):
    list.rotate(-k + 1)
    print(", {}".format(list.popleft()), end="")
print(">")