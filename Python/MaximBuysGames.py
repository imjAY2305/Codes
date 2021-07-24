sam = list(map(int,input().split()))
g = sam[0]
w = sam[1]
games = list(map(int,input().split()))
wallet = list(map(int,input().split()))
c = 0
point = 0
for i in range(w):
    if(point<g):
        for j in range(g):
            print(wallet[0],games[point],point,c)
            if(wallet[0]>=games[point]):
                c += 1
                wallet.pop(0)
                point += 1
                break
            else:
                point += 1
    else:
        break
print(c)