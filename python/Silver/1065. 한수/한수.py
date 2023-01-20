import sys

def d(a):
    a_list = list(map(int,str(a)))
    if a < 100:
        return 1
    elif a_list[0] - a_list[1] == a_list[1] - a_list[2]:
        return 1
    else :
        return 0

count = 0
c = int(sys.stdin.readline())
for i in range(1, c + 1):
    count += d(i)
    
print(count)