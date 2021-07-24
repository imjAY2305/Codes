n = int(input())
arr =[]
f = 1
for i in range(n):
    x = input()
    arr.append(x)
for i in range(n-1):
    if (arr[0][0] != arr[n-1][len(arr[n-1])-1]) or (arr[i][len(arr[i])-1] != arr[i+1][0]):
        f = 0
        break
if(f):
    print("Can be formed")
else:
    print("Cannot be Formed")