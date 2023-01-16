import sys

n, score, p = map(int, sys.stdin.readline().split())
count = 0
result = -1

if n != 0:
    score_list = list(map(int, sys.stdin.readline().split()))
    del score_list[n:]

    score_list.sort(reverse=True)

    for i in score_list:
        if score == i:
            count += 1
        if score > i:
            result = score_list.index(i) + 1 - count
            break
    if result == -1 and n < p:
        result = n + 1 - count
else:
    result = 1

print(result)