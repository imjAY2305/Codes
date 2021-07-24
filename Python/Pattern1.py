s = int(input())
n = int(input())
c = 1
print()
arr = [[]for i in range(n)]
for i in range(s,s+n):
    for j in range(c):
        arr[c-1].append(i)
    c += 1
c = 0
for i in range(n):
    for j in arr[c]:
        print(j,end="")
    c += 1
    print()
arr.pop()
c = n-2
for i in range(n-1):
    for j in arr[c]:
        print(j,end="")
    c -= 1
    print()

#
3
4

3        
44       
555      
6666     
555      
44       
3
#