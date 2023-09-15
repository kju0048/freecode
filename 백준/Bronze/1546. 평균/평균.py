import sys

n = int(sys.stdin.readline())
nList = list(map(int, sys.stdin.readline().split()))
del nList[n:]
maxList= max(nList)

print("{}".format(sum(nList) / maxList * 100 / n))