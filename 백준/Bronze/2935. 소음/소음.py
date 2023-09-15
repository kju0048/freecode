import sys

s = [0, 0, 0]
for i in range(3):
    s[i] = sys.stdin.readline().strip('\n')


if s[1] == '*':
    print(int(s[0]) * int(s[2]))
elif s[1] == '+':
    print(int(s[0]) + int(s[2]))