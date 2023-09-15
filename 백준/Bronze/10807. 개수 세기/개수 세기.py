import sys

count = int(sys.stdin.readline())
llist = [int (x) for x in sys.stdin.readline().split()]
find = int(sys.stdin.readline())

vCount = 0

for i in range(0, count):
    if llist[i] == find:
        vCount += 1

print(vCount)