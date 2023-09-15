import sys
inp = sys.stdin.readline

setList = [x for x in range(1, 9)]

numList = list(map(int, inp().split()))

if setList == numList:
    print("ascending")
elif numList == list(reversed(setList)):
    print("descending")
else:
    print("mixed")