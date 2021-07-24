n = int(input())
suma = 0
ca = 0
sumb = 0
cb = 0
for i in range(n):
    sam = list(map(int,input().split()))
    t = sam[0]
    m = sam[1]
    l = sam[2]
    if(t==1):
        suma += m
        ca += 10
    else:
        sumb += m
        cb += 10
if(suma>=ca//2):
    print("LIVE")
else:
    print("DEAD")
if(sumb>=cb//2):
    print("LIVE")
else:
    print("DEAD")