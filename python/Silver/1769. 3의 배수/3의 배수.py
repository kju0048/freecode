import sys

inp = sys.stdin.readline
n = int(inp())
count = 0

while n >= 10:
    n = sum(map(int, str(n)))
    count += 1


print(count)
if n%3 == 0:
    print('YES')
else:
    print('NO')