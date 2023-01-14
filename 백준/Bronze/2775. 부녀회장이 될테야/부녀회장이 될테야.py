import sys



case = int(sys.stdin.readline())

for _ in range(case):
    floor = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    list_A = [i for i in range(1, n + 1)]

    for k in range(floor):
        for p in range(1, n):
            list_A[p] += list_A[p-1]

    print(list_A[n-1])