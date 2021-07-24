def prime(n):
    c = 1
    if(n%2==0):
        return False
    else:
        for i in range(3,n//2):
            if(n%i==0):
                c += 1
                break
        if(c==1):
            return True
        else:
            return False

t = int(input())
for x in range(t):
    n = int(input())
    c = 1
    while(True):
        before = n-c
        after = n+c
        if(prime(before) and prime(after)):
            print(min(before,after))
            break
        elif(prime(before)):
            print(before)
            break
        elif(prime(after)):
            print(after)
            break
        c += 1