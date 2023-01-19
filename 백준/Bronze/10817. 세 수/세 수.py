import sys

s = list(map(int, sys.stdin.readline().split()))

s.sort()

print(s[1])