import sys

nList = []
count = 0
for i in range(10):
    num = int(sys.stdin.readline())
    if not(num%42 in nList):
        count+=1
        nList.append(num%42)

print(count)