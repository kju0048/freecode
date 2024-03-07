# 1377
import sys

input = sys.stdin.readline

N = int(input())
lista = []
count = 1

for i in range(N):
    lista.append((int(input()), i))
    
max_n = 0
lista_sort = sorted(lista)
for i in range(N):
    if max_n < lista_sort[i][1] - i:
        max_n = lista_sort[i][1] - i
        
print(max_n+1)
