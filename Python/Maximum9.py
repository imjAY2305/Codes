t = int(input())
for x in range(t):
    arr = list(map(int,input().split()))
    n = arr[0]
    k = arr[1]
    num = input()
    res = []
    for i in num:
        new = num.replace(i,"")
        res.append(int(new)%k)
    print(max(res))
    