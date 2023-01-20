import sys

s = [False for i in range(30)]

for i in range(28):
    s[int(sys.stdin.readline()) - 1] = True

for y in range(30):
    if not s[y]:
        print(y+1)