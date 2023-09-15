import sys

s = sys.stdin.readline().strip('\n')
s_list = list(s)
count = 0

for i in s_list :
    if i == 'A' or i == 'B' or i =='C':
        count += 3
    elif i == 'D' or i == 'E' or i =='F':
        count += 4
    elif i == 'G' or i == 'H' or i =='I':
        count += 5
    elif i == 'J' or i == 'K' or i =='L':
        count += 6
    elif i == 'M' or i == 'N' or i =='O':
        count += 7
    elif i == 'P' or i == 'Q' or i =='R' or i == 'S':
        count += 8
    elif i == 'T' or i == 'U' or i =='V':
        count += 9
    elif i == 'W' or i == 'X' or i =='Y' or i == 'Z':
        count += 10
        
print(count)