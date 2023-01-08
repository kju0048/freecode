import sys
inp = sys.stdin.readline

n = int(inp())
count = 0
if n != 0:
    nList = list(map(int, inp().split()))
    del nList[n:]

    for i in nList:
        for j in range(2, i+1):
            if i == j:
                count += 1
            if i % j == 0:
                break

print(count)
