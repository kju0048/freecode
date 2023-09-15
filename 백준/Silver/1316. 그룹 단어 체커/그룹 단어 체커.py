import sys

rep = int(sys.stdin.readline())
count = 0
out = 0
for i in range(rep) :
    str = sys.stdin.readline().strip('\n')
    out = 0
    for i in str:
        str = str.replace(i, '*')
        check = 0
        for j in str:
            if j == '*' and check == 1:
                count += 1
                out = 1
                break
            if j != '*':
                check = 1
        
        if out == 1:
            break

print(rep - count)