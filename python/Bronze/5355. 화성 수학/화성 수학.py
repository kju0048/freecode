import sys

ret = int(sys.stdin.readline())
for i in range(ret): 
    s = list(sys.stdin.readline().split())
    s[0] = float(s[0])
    res = s[0]
    for i in s:
        if i == '@':
            res *= 3
        elif i == '%':
          res += 5
        elif i == '#':
          res -= 7
    print("{:.2f}".format(res))