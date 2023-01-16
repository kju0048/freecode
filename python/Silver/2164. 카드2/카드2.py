import sys
from collections import deque
inp = sys.stdin.readline

n = int(inp())

queueL = deque([x for x in range (1, n+1)])

while(len(queueL) != 1):
    queueL.popleft()
    queueL.append(queueL[0])
    queueL.popleft()

print(queueL[0])
