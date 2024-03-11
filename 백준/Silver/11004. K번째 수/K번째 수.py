# 11004
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
lista = list(map(int, input().split()))

def swap(a, b):
    global lista
    lista[a], lista[b] = lista[b], lista[a]
    
def quick_sort(left, right, k):
    global lista
    
    if left < right:
        pivot = partition(left, right)
        if pivot == k:
            return
        elif k < pivot:
            quick_sort(left, pivot-1, k)
        else:
            quick_sort(pivot+1, right, k)

def partition(l, r):
    global lista
    
    if l + 1 == r:
        if lista[l] > lista[r]:
            swap(l, r)
        return r
    
    m = (l + r) // 2
    swap(l, m)
    
    pivot = lista[l]
    i, j = l+1, r
    while i <= j:
        while pivot < lista[j] and j > 0:
            j -= 1
        while pivot > lista[i] and i < len(lista) - 1:
            i += 1
        if i <= j:
            swap(i, j)
            i += 1
            j -= 1
    lista[l] = lista[j]
    lista[j] = pivot
    return j

quick_sort(0, n-1, k-1)
print(lista[k-1])