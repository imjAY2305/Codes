def divide(n):
    return n//2
arr = list(map(int,input().split()))
n = len(arr)
for i in range(len(arr)):
    if(arr[i]%2!=0 and arr[i]!=1):
        arr[i] -= 1
        n += 1
if(1 in arr):
    arr.remove(1)
arr.sort()
ref = min(arr)
for i in range(1,len(arr)):
    while(arr[i]!=ref):
        arr[i] //= 2
        n += 1
while(1 not in arr):
    arr = list(map(divide,arr))
    n += 1
print(n)