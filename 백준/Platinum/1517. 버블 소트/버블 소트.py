import sys
inp = sys.stdin.readline

count = 0

def merge_sort(start, end):
    global count, nList

    if start < end:
        middle = (start + end) // 2
        merge_sort(start, middle)
        merge_sort(middle+1, end)

        left, right = start, middle + 1
        temp = []

        while left <= middle and right <= end:
            if nList[left] <= nList[right]:
                temp.append(nList[left])
                left += 1
            else:
                temp.append(nList[right])
                right += 1
                count += (middle - left + 1)

        if left <= middle:
            temp = temp + nList[left:middle + 1]
        if right <= end:
            temp = temp + nList[right:end + 1]

        for i in range(len(temp)):
            nList[start + i] = temp[i]

n = int(inp())
nList = list(map(int, inp().split()))
merge_sort(0, n-1)
print(count)