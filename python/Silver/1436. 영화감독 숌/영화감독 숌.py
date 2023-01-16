import sys
inp = sys.stdin.readline

sel = int(inp())
count = 0
num = 666
while count != sel:
    if '666' in str(num):
        count +=1
    num += 1

print(num - 1)
