import sys
inp = sys.stdin.readline

for i in range(int(inp())):
    count = 0
    pss = list(map(str, inp().strip()))
    for j in pss:
        if j == '(':
            count += 1
        else:
            count -= 1

        if count < 0:
            break
    
    if count == 0:
        print("YES")
    else:
        print("NO")
