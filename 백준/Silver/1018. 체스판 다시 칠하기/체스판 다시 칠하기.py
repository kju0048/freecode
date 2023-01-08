import sys
inp = sys.stdin.readline

min = 64

def checkError(CL, i, j):
    global min
    Check = 0
    for n in range(8):
        for m in range(8):
            if ((i+j+n+m)%2 == 0) and (CL[i+n][j+m] == 'B'):
                Check += 1
            elif ((i+j+n+m)%2 == 1) and (CL[i+n][j+m] == 'W'):
                Check += 1
    if Check > 32:
        Check = 64 - Check
    if Check < min:
        min = Check


n, m = map(int, inp().split())
CL = [['W' for j in range(m)] for i in range(n)]

for y in range(n):
    CL[y] = list(inp().strip())

for i in range(0, n-7):
    for j in range(0, m-7):
        checkError(CL, i, j)

print(min)