import sys

inp = sys.stdin.readline

n = int(inp())

info = [list(map(str, inp().split())) for i in range(n)]
info.sort(key=lambda x:int(x[0]))

for outp in info:
    print(outp[0], outp[1])