# 17298
import sys
from queue import PriorityQueue

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())


que = PriorityQueue()

for _ in range(N):
    num = int(input())
    if num == 0:
        if que.empty():
            print('0\n')
        else:
            temp = que.get()
            print(str(temp[1]) + '\n')
    else:
        que.put((abs(num), num))
