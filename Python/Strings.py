arr = list(map(str,input().split()))
vowels  = ["a","e","i","o","u"]
for i in range(len(arr[0])):
    if(arr[0][i] in vowels):
        print("$",end="")
    else:
        print(arr[0][i],end="")
print()
for i in range(len(arr[1])):
    if(arr[1][i] not in vowels):
        print("*",end="")
    else:
        print(arr[1][i],end="")
print()
print(arr[2].upper())