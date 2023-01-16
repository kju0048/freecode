import sys

inp = sys.stdin.readline
mul = 1
for i in range(3):
    mul *= int(inp())

nList = list(map(int, str(mul)))

for i in range(0, 10):
    print(nList.count(i))