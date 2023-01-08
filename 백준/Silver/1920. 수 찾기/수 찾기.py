import sys
inp = sys.stdin.readline

def binary_search(i, aList, start, end):
    if start > end:
        return 0

    middle = (end + start) // 2

    if i > aList[middle]:
        return binary_search(i, aList, middle + 1, end)
    elif i < aList[middle]:
        return binary_search(i, aList, start, middle - 1)
    else:
        return 1


n = int(inp())
aList = list(map(int, inp().split()))
aList.sort()

m = int(inp())
bList = list(map(int, inp().split()))


for i in bList:
    print(binary_search(i, aList, 0, n - 1))