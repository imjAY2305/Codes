n = int(input())
arr = []
for i in range(n):
    ref = list(map(int,input().split()))
    arr.append(ref)
print(arr)
res = []
c = 0
for i in range(n):
    ref = []
    for j in range(n-1,-1,-1):
        ref.append(arr[j][c])
    res.append(ref)
    c = c+1
print(res)    