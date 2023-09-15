def solution(arr):
    del arr[arr.index(min(arr))]
    
    if len(arr) < 1:
        return [-1]
    else:
        return arr