n = int(input())
arr = list(map(int,input().split()))
c = 0
for i in range(1,n+1):
    if(n*i in arr):
        c+=1
print(c)