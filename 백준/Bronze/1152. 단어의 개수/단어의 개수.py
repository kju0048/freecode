import sys

str = list(sys.stdin.readline().strip().strip('\n').split(' '))

if '' in str:
    print(0)
else :
    print(len(str))