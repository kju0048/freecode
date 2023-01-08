import sys
from functools import reduce
inp = sys.stdin.readline

n, k = map(int, inp().split())

if k > 0:
    print(int(reduce(lambda x, y: x * y, [x for x in range(n, n-k, -1)]) / reduce(lambda x, y: x * y, [x for x in range(1, k+1)])))
else:
    print(1)
