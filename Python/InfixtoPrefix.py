stack = [0]
def precedenace(a):
    if a=='(':
        return 1
    if a=='+' or a=='-':
        return 2
    if a=='*' or a=='/':
        return 3
    return 1
st = input()
i = 0
x = ''
if (st.count('(')==st.count(')')):
    while(i<len(st)):
        if st[i].isalnum():
            print(st[i],end="")
        elif st[i]=='(':
            stack.append(st[i])
        elif st[i]==')':
            x = stack.pop()
            while(x!='('):
                print(x,end="")
                x = stack.pop()
        else:
            while(precedenace(stack[-1])>=precedenace(st[i])):
                print(stack.pop(),end="")
            stack.append(st[i])
        i += 1
    while(len(stack)!=1):
        print(stack.pop(),end="")
else:
    print("Invalid Expression, Parenthesis not matched.")