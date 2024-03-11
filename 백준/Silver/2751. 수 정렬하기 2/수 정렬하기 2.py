import sys
from collections import deque
inp = sys.stdin.readline


nList = []
for i in range(int(inp())):
    nList.append(int(inp()))
nList.sort()
for i in nList:
    print(i)
