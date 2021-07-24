n = int(input())
c = 0
while(n>1):
    if(n%3==0):
        c += 1
        n /= 3
    else:
        c += 1
        n -= 1
print(c)
print("After Git update")