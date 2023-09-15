import sys

n = int(sys.stdin.readline())

for i in range(n) :
    count = 0
    nList = list(map(int, sys.stdin.readline().split()))
    del nList[nList[0] + 1 : ]
    average = (sum(nList) - nList[0]) / nList[0]
    for i in range(1, len(nList)):
        if nList[i] > average:
            count += 1
    print("{:.3f}%".format(float(count)/(nList[0]) * 100))