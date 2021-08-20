n = int(input())
arr = list(map(int,input().split()))
profit = arr[0]
ref = arr[0]
print(arr,profit,ref)
for i in range(1,n):
    if(arr[i]%ref==0):
        profit = profit+arr[i]
        ref = arr[i]
print(profit)