import sys

n = int(sys.stdin.readline())
i = 1
while n - i >= 0:
    n -= i
    i += 1

print(i - 1)
