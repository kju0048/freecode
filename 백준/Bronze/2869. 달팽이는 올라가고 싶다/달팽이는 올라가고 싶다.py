import sys

a, b, v = map(int, sys.stdin.readline().split())

print((v-a-1) // (a - b) + 2)