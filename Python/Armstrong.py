num = int(input())
n = len(str(num))
sum = 0
for i in str(num):
    sum = sum + (int(i)**n)
if(sum==num):
    print("Armstrong",num,sum)
else:
    print("Not Armstrong",num,sum)