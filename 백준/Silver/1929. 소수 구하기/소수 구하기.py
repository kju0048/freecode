import sys

inp = sys.stdin.readline

def primeCheck(i):
    if i == 1:
        return
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            return
    primeL.append(i)
    print(i)


m, n = map(int, inp().split())

primeL = []

for i in range(m, n+1):  
    primeCheck(i)