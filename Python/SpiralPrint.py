sam = list(map(int,input().split()))
r = sam[0]
c = sam[0]
arr = []
for i in range(r):
    arr.append(list(map(int,input().split())))
k=0
l=0
m = r
n = c
while(k<r and l<c):
    for i in range(l,n):
        print(arr[k][i],end=" ")
    k += 1
    for i in range(k,m):
        print(arr[i][n-1],end=" ")
    n -= 1
    if(k<m):
        for i in range(n-1,l-1,-1):
            print(arr[m-1][i],end=" ")
        m -= 1
    if(l<n):
        for i in range(m-1,k-1,-1):
            print(arr[i][l],end=" ")
        l += 1