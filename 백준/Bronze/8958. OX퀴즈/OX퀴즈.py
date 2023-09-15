import sys

n = int(sys.stdin.readline())

for i in range(n):
    nList = list(sys.stdin.readline().strip('\n'))
    count = 0
    cont = 0
    for st in nList :
        if st == 'O':
            cont += 1
            count += cont
        else :
            cont = 0
    print(count)