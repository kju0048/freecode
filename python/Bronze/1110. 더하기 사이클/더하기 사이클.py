import sys

count = 0
setN = num = int(sys.stdin.readline())

while 1:
    if num < 10:
        nlist = [0, num]
    else:
        nlist = list(map(int, str(num)))
    num = nlist[1]*10 + (nlist[1] + nlist[0]) % 10
    count += 1

    if setN == num :
        break
print(count)