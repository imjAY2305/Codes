from itertools import combinations as c
a = input()
res = []
for i in a:
    res.append(i)
arr = []
for i in range(1,len(a)+1):
    comb = c(res,i)
    arr.extend(list(comb))
res = []
for i in arr:
    s = "".join(list(i))
    res.append(s)
print(" ",end="")
res.sort()
for i in res:
    print(i,end=" ")






s = input()
s2 = ['']
for i in range(1, len(s) + 1):
    s1 = c(s, i)
    for i in s1:
        s2.append("".join(i))
print(*sorted(sorted(s2))) 