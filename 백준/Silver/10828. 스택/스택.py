import sys

inp = sys.stdin.readline

stack = []
for i in range(int(inp())):
    m = inp().strip()

    if m.find(' ') != -1:
        m, n = m.split()

    if m == "push":
        stack.append(n)
    elif m == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif m == "size":
        print(len(stack))
    elif m== "empty":
        print("1" if len(stack) == 0 else "0")
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack) - 1])