import sys
inp = sys.stdin.readline

n = int(inp())
nL = [0 for _ in range(n)]
modeL = {}

for i in range(0, n):
    nL[i] = int(inp())
    if nL[i] in modeL:
        modeL[nL[i]] += 1
    else:
        modeL[nL[i]] = 1
    
modeV = max(modeL, key=modeL.get)
exList = [i for i, j in modeL.items() if j == modeL[modeV]]

exList.sort(reverse=False)
nL.sort(reverse=False)

print(round(sum(nL) / n)) # 산술평균
print(nL[n//2]) # 중앙값
if len(exList) == 1:
    print(modeV) # 최빈값
else:
    print(exList[1])
print(nL[n-1] - nL[0]) # 범위