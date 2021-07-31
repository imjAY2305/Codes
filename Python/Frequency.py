arr = list(map(int,input().split()))
ref = list(set(arr))
ref.sort()
res = []
for i in ref:
    sam = []
    sam.append(i)
    sam.append(arr.count(i))
    res.append(sam)
Dict = dict(res)
for i in Dict.keys():
    print(i,Dict[i])