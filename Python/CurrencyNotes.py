n = int(input())
temp = n
c = 0
while(temp>0):
    if(temp>=1000):
        temp -= 1000
        c += 1
    elif(temp>=500):
        temp -= 500
        c += 1
    elif(temp>=100):
        temp -= 100
        c += 1
    elif(temp>=50):
        temp -= 50
        c += 1
    elif(temp>10):
        temp -= 10
        c += 1
    else:
        c += temp
        temp -= temp
print(c)  