arr = list(map(int,input().split()))
n = len(arr)
ref = []
for i in range(1,n):
    if(sum(arr[0:i])==sum(arr[i+1:n+1])):
        ref.append(arr[i])
        print("Inside IF",sum(arr[0:i]),sum(arr[i+1:n+1]))
    print(sum(arr[0:i]),sum(arr[i+1:n+1]))
print(min(ref))