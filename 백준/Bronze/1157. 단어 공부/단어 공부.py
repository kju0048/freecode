import sys

str = sys.stdin.readline().strip('\n')
str_list = list(str)
dict = {}

for i in str_list:
    if i.upper() not in dict:
        dict[i.upper()] = 0
    dict[i.upper()] += 1
sMax = [k for k,v in dict.items() if max(dict.values()) == v]
if len(sMax) != 1:
    print('?')
else :
    print(sMax[0])