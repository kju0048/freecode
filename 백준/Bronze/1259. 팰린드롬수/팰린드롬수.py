import sys
inp = sys.stdin.readline
numList = []

def input_num():
    global numList
    numList.clear()
    for i in inp().strip():
        numList.append(i)
    return numList

while ['0'] != input_num():
    if numList == list(reversed(numList)):
        print("yes")
    else:
        print("no")
