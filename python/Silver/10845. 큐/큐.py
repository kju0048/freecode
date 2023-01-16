import sys
from collections import deque

inp = sys.stdin.readline

que = deque()
for i in range(int(inp())):
    m = inp().strip()

    if m.find(' ') != -1:
        m, n = m.split()

    if m == "push":
        que.appendleft(n)
    elif m == "pop":
        if len(que) == 0:
            print(-1)
        else:
            print(que.pop())
    elif m == "size":
        print(len(que))
    elif m== "empty":
        print("1" if len(que) == 0 else "0")
    elif m == "back":
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    else:
        if len(que) == 0:
            print(-1)
        else:
            print(que[len(que) - 1])