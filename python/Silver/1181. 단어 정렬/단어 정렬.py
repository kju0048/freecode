import sys
from functools import reduce
inp = sys.stdin.readline

wordL = []

for i in range(int(inp())):
    word = inp().strip()
    if word not in wordL:
        wordL.append(word)

wordL.sort()
wordL.sort(key=len)

for i in wordL:
    print(i)