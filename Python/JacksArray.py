from itertools import combinations as c
n = int(input())
arr = list(map(int,input().split()))
res = []
for i in range(2,n+1):
    sam = c(arr,i)
    for j in sam:
        if(sum(j)==0):
            res.append(len(j))
print(max(res))