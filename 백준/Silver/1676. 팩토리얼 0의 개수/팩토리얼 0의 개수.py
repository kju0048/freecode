import sys

check = True
result = 0
sum = 1
input_int = int(sys.stdin.readline())
for i in range(1, input_int+1) :
    sum *= i

if input_int == 0:
    check = False

while(check==True):
    if sum % 10 == 0:
        result += 1
        sum //= 10
    else:
        check = False

print(result)