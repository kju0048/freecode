import sys

inp = sys.stdin.readline

def binary_search(nL, key, start, end):
    if start > end:
        return 0

    middle = (end + start) // 2

    if key > nL[middle]:
        return binary_search(nL, key, middle + 1, end)
    elif key < nL[middle]:
        return binary_search(nL, key, start, middle - 1)
    else:
        return dict1.get(key)

n = int(inp())
numL = sorted(list(map(int, inp().split())))

m = int(inp())
cardL = list(map(int, inp().split()))

dict1 = {}

for i in numL:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1

for i in cardL:
    print(binary_search(numL, i, 0, n-1), end=' ')