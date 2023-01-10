import sys

str = sys.stdin.readline().strip('\n')
str_list = list(str)
nList = [-1 for i in range(26)]
for i in range(0, len(str_list)):
    if nList[ord(str_list[i]) - 97] == -1 :
        nList[ord(str_list[i]) - 97] = i

for i in nList:
    print(i, end=' ')