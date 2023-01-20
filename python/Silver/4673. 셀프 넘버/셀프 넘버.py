import sys

def d(a):
    a_list = list(map(int,str(a)))
    return a + sum(a_list)

nList = list(map(int, range(1, 10001)))
for i in range(1, 10001):
    if d(i) in nList:
        nList.remove(d(i))

for i in nList:
    print(i)