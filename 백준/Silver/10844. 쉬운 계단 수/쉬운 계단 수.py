<<<<<<< HEAD:bj/b10844.py
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
=======
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
>>>>>>> 96df4213db17be9234b309045ea54ef0749ac768:백준/Silver/10844. 쉬운 계단 수/쉬운 계단 수.py
