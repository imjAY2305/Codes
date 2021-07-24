n = int(input())
str1 = input()
res = []
for i in range(0,n+1):
    for j in range(i+1,n+1):
        res.append(str1[i:j])
c = 0
for i in range(len(res)):
    if(int("".join(res[i]))%2==0):
        c+=1
print(c)