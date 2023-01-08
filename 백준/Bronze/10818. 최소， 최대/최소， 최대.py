import sys

n = int(sys.stdin.readline())
nList = [int(x) for x in sys.stdin.readline().split()]
del nList[n:]
nList.sort()
print("{} {}".format(nList[0], nList[n-1]))