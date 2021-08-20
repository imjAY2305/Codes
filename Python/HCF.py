ref = list(map(int,input().split()))
a = ref[0]
b = ref[1]
gcd = 0
i = 1
while i<=a and i<b:
    if(a%i==0 and b%i==0):
        gcd = i
    i = i+1
print("HCF is :",gcd)