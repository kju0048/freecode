# 11659 
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lista = [[0] * n]
listsum = [[0] * (n+1)]
for i in range(n):
    lista.append([0] + list(map(int, input().split())))

for i in range(n):
    listtemp = [0]
    tempsum = 0
    for j in range(n):
        tempsum += lista[i+1][j]
        listtemp.append(tempsum + listsum[i][j+1] + lista[i+1][j+1] )
    listsum.append(listtemp)

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(listsum[x2][y2] - listsum[x1-1][y2] - listsum[x2][y1-1] + listsum[x1-1][y1-1])
