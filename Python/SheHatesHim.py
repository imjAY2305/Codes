t = int(input())
a = '*'
for i in range(t):
    n = int(input())
    ref = n*2
    arr = [[]for i in range(n)]
    for j in range(0,n):
        arr[j].append((j+1)*a)
        for k in range(j,ref-len((j+1)*a)-1):
            arr[j].append('#')
        arr[j].append((j+1)*a)
    for x in arr:
        for y in x:
            print(y,end="")
        print()
    print()