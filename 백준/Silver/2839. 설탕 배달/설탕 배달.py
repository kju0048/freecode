import sys

su = int(sys.stdin.readline())

take = 0
while su >= 0:
    if su % 5 == 0:
        take += (su // 5)
        print(take)
        break
    su -= 3
    take += 1
else :
    print(-1)