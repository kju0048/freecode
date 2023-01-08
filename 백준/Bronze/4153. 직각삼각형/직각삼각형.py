import sys
inp = sys.stdin.readline
numList = []

def input_num():
    global numList
    numList = sorted(list(map(int, inp().split())))
    return numList

while [0, 0, 0] != input_num():
    if numList[0]**2 + numList[1]**2 == numList[2]**2:
        print("right")
    else:
        print("wrong")
