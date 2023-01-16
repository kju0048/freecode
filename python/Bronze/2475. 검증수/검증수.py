import sys

inp = sys.stdin.readline

list = list(map(int, inp().split()))

print(sum(x**2 for x in list) % 10)