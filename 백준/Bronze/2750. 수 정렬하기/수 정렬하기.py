# 2750
import sys

input = sys.stdin.readline

N = int(input())
lista = []

for i in range(N):
    lista.append(int(input()))

for i in range(N-1, 0, -1):
    for j in range(i):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]
for i in range(N):
    print(lista[i])