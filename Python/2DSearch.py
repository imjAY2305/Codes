sam = list(map(int,input().split()))
R = sam[0]
C = sam[1]
arr = []
for i in range(R):
    x = list(map(int,input().split()))
    arr.append(x)
search = int(input())
for i in arr:
    if(search in i):
        print(True)
        break
else:
    print(False)