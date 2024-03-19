# 11724
import sys
sys.setrecursionlimit(10000) # 재귀 반복 횟수 제한(기본값 1000)
input = sys.stdin.readline

n, e = map(int, input().split())

A = [[] for _ in range(n+1)]
visited = [False] * (n+1)

def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)
            
for _ in range(e):
    x, y = map(int, input().split())
    A[x].append(y)
    A[y].append(x)
    
count = 0

for i in range(1, n+1):
    if not visited[i]:
        count += 1
        DFS(i)

print(count)
