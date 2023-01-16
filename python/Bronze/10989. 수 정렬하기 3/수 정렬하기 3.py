import sys
inp = sys.stdin.readline

nList = [0] * 10001

for _ in range(int(inp())):
    nList[int(inp())] += 1

for i in range(10001):
    for j in range(nList[i]):
        print(i)