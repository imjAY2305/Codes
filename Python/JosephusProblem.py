n = int(input())
k = int(input())
arr = [i for i in range(1,n+1)]
c = 0
while(len(arr)!=1):
    for i in range(k-1):
        c+=1
        if(c==len(arr)-1):
            c = -1
    arr.remove(arr[c-1])
    print(arr, c)
    c -= 1
print(arr)