import sys
inp = sys.stdin.readline

l = int(inp())
str1 = inp().strip()
h = 0

for i in range(l):
    h += (ord(str1[i]) - 96) * (31 ** i)

print(h % 1234567891)