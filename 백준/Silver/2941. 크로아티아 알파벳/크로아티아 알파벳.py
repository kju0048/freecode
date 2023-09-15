import sys

cr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = sys.stdin.readline().strip('\n')

for i in cr :
    s = s.replace(i, '*')  
print(len(s))