import sys
inp = sys.stdin.readline

a, b = map(int, inp().split())

gcm = 1

for i in range(1, (a if a<b else b) + 1):
    if a%i == 0 and b%i ==0:
        gcm = i

print(gcm)
print(gcm * (a//gcm) * (b//gcm))