t = int(input())
for x in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    res = []
    c = 0
    q = int(input())
    sa = list(map(int,input().split()))
    ea = list(map(int,input().split()))
    for i in range(q):
        s = sa[i]
        e = ea[i]
        for j in range(e):
            res.append(arr[c])
            c += 1
            if(c==n):
                c = 0
        print(sum(res[s-1:e]),end=" ")
    print()