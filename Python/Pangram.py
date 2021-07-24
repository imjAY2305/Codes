n = int(input())
string = input()
str1 = string.lower()
arr = [chr(i) for i in range(ord('a'),ord('z')+1)]
ref = True
for i in range(len(arr)):
    if(arr[i] not in str1):
        ref = False
        break
if(ref):
    print("YES")
else:
    print("NO")