n = int(input())
arr = list(map(int,input().split()))
c = 0
for i in range(n-1):
    for j in range(i+1,n):
        if((arr[i]+arr[j]) in arr[j:n]):
            c+=1
print(c)