ref = list(map(int,input().split()))
a = ref[0]
b = ref[1]
lcm = max(a,b)
while True:
    if(lcm%a==0 and lcm%b==0):
        print("LCM is :",lcm)
        break
    else:
        lcm = lcm+1