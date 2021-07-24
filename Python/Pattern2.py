n = int(input())
c = 1
p = 1
arr = [[]for i in range(n)]
for i in range(n):
    for j in range(c):
        arr[i].append(p)
        p += 1
        arr[i].append('*')
    c+=1
for i in range(n):
    arr[i].pop()
    if(i%2!=0):
        for j in arr[i][::-1]:
            print(j,end="")
        print()
    else:
        for j in arr[i]:
            print(j,end="")
        print()

#
5
1
3*2
4*5*6
10*9*8*7
11*12*13*14*15
#