a = list(map(str,input().split()))
t = int(a[1])
res = []
for i in range(t):
    n = input()
    res.append(a[0].count(n))
for i in res:
    print(i)