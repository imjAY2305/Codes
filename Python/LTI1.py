str1 = input()
ref = input()
while True:
    if ref in str1:
        str1 = str1.replace(ref,'')
        print(ref in str1)
    else:
        break
print(str1)