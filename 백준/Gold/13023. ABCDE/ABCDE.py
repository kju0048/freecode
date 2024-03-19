import sys
sys.setrecursionlimit(10000) # 재귀 반복 횟수 제한(기본값 1000)
input = sys.stdin.readline

n, m = map(int, input().split())

fgraph = [[] for _ in range(n)]
bCheck = [False] * n
endCheck = False

for _ in range(m):
    x, y = map(int, input().split())
    fgraph[x].append(y)
    fgraph[y].append(x)

def DFS(num, count):
    global endCheck
    if count == 5:
        endCheck = True
        return
    bCheck[num] = True
    for i in fgraph[num]:
        if not bCheck[i]:
            DFS(i, count + 1)
    bCheck[num] = False

for i in range(n):
    DFS(i, 1)
    if endCheck:
        break

if endCheck:
    print(1)
else:
    print(0)