import sys
from collections import deque

inp = sys.stdin.readline

deque1 = deque()
for i in range(int(inp())):
    m = inp().strip()

    if m.find(' ') != -1:
        m, n = m.split()

    if m == "push_back":
        deque1.appendleft(n)
    elif m == "push_front":
        deque1.append(n)
    elif m == "pop_front":
        if len(deque1) == 0:
            print(-1)
        else:
            print(deque1.pop())
    elif m == "pop_back":
        if len(deque1) == 0:
            print(-1)
        else:
            print(deque1.popleft())
    elif m == "size":
        print(len(deque1))
    elif m== "empty":
        print("1" if len(deque1) == 0 else "0")
    elif m == "back":
        if len(deque1) == 0:
            print(-1)
        else:
            print(deque1[0])
    else:
        if len(deque1) == 0:
            print(-1)
        else:
            print(deque1[len(deque1) - 1])

        