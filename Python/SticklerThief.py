a = list(map(int,input().split()))
sum = 0
while(len(a)>0):
    sum += max(a)
    i = a.index(max(a))
    if(i==0):
        del a[i:i+2]
    elif(i==len(a)-1):
        del a[i-1:i+1]
    else:
        del a[i-1:i+2]
print(sum)