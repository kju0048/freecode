import sys

n = int(sys.stdin.readline())

nL = [[0] * 10 for _ in range(n)]
nL[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1, n):
    nL[i][0] = nL[i-1][1]
    nL[i][9] = nL[i-1][8]

    for j in range(1, 9):
        nL[i][j] = nL[i-1][j-1] + nL[i-1][j+1]

print(sum(nL[n-1])%1000000000)
