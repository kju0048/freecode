# 12891
import sys
input = sys.stdin.readline

s, p = map(int, input().split())
dna = input()
lista = list(map(int, input().split()))
dicd = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
checkCount = 0
dnaCount = [0] * 4
res = 0

for i in lista:
    if i == 0:
        checkCount += 1

for i in dna[:p]:
    dnaCount[dicd[i]] += 1
    if dnaCount[dicd[i]] == lista[dicd[i]]:
        checkCount += 1

if checkCount == 4:
    res += 1
    
for p2 in range(p, s):
    p1 = p2 - p

    dnaCount[dicd[dna[p2]]] += 1
    if dnaCount[dicd[dna[p2]]] == lista[dicd[dna[p2]]]:
        checkCount += 1
    
    if dnaCount[dicd[dna[p1]]] == lista[dicd[dna[p1]]]:
        checkCount -= 1
    dnaCount[dicd[dna[p1]]] -= 1
        
    if checkCount == 4:
        res += 1
        
print(res)