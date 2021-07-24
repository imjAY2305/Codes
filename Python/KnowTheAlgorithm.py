a = list(map(int,input().split()))
n = a[0]
c = a[1]
pi = list(map(int,input().split()))
ti = list(map(int,input().split()))
sumL=0
timeL = 0
sumR=0
timeR = 0
for i in range(n):
    timeL += ti[i]
    sumL += max(0,(pi[i]-c*timeL))
    timeR += ti[n-i-1]
    sumR += max(0,(pi[n-i-1]-c*timeR))
if sumL>sumR:
    print("Limak")
elif sumR>sumL:
    print("Radewoosh")
else:
    print("Tie")