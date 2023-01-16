import sys
inp = sys.stdin.readline

n = int(inp())
res = 0

for i in range(1, n+1):
    lSum = list(map(int, str(i)))
    sSum = i + sum(lSum)
    if n == sSum:
        res = i
        break

print(res)