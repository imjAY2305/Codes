n = int(input())
arr = list(map(int,input().split()))
arr.sort()
print(arr)
flag = True
for i in range(n):
    if(sum(arr[0:i])==sum(arr[i:n])):
        flag = True
        break
    else:
        flag = False
if(flag):
    print("YES")
else:
    print("NO")