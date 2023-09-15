import sys

inp = sys.stdin.readline

x, y, w, h = map(int, inp().split())

print(min(x, y, abs(x-w), abs(y-h)))