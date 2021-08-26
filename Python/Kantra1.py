arr = list(map(int,input().split()))
n = len(arr)
arr.sort()
ref = []
for i in range(n-1):
    ref.append(abs(arr[i]-arr[i+1]))
max1 = 0
for i in range(len(ref)):
    if(ref[i]>max1):
        max1 = ref[i]
print(max1)