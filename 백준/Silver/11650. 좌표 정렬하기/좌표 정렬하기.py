import sys

inp = sys.stdin.readline

n = int(inp())

arr = []

for i in range(n):
    arr.append(list(map(int, inp().split())))

arr.sort()

for i in range(n):
    print(arr[i][0], arr[i][1])