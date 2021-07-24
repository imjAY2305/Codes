n = int(input())
a = int(input())
CL = []
capacity = []
SR = []
SY = []
for i in range(a):
    str1 = str(input())
    res = str1.split(" ")
    CL.append(res[0])
    SR.append(int(res[1]))
    capacity.append(int(res[2]))
    SY.append(int(res[2]))
b = int(input())
SC = []
DT = []
for i in range(b):
    str1 = str(input())
    res = str1.split("_")
    SC.append(res[0])
    DT.append(res[1])
    
#LOGIC

water = 0
for i in range(n):
    if(0 not in capacity):
        for j in range(len(CL)):
            water += SR[j]
            capacity[j] -= SR[j]
    else:
        loc = capacity.index(0)
        loc1 = DT.index(CL[loc])
        s = SC[loc1]
        d = CL[loc]
        if(s!="F"):
            loc2 = CL.index(s)
            capacity[loc2] = 0
            water += SY[loc2]
            water += SY[CL.index(d)]
        else:
            water += SY[CL.index(d)]
print(water+sum(SR))
            
