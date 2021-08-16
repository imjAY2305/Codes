t = int(input())
for x in range(t):
    ref = list(map(int,input().split()))
    n = ref[0]
    k = ref[1]
    arr =list(map(int,input().split()))
    for i in arr:
        if(i<=k):
            print("1",end="")
            k = k-i
        else:
            print("0",end="")
    print()