import sys
inp = sys.stdin.readline

n, m = map(int, inp().split())
max = 0
cList = list(map(int, inp().split()))
del cList[n:]
cList.sort()

for i in range(n):
    if cList[i] > m:
        break
    for j in range(i):
        if cList[i] + cList[j] > m:
            break
        for p in range(j):
            if cList[i] + cList[j] + cList[p] > m:
                break
            if cList[i] + cList[j] + cList[p] > max:
                max = cList[i] + cList[j] + cList[p]

print(max)