#include<iostream>
#include<bits/stdc++.h>
#include<string>
using namespace std;

int precedence(char a)
{
    if(a=='(')
        return 0;
    if(a=='+' || a=='-')
        return 1;
    if(a=='*' || a=='/')
        return 2;
    return 0;
}

int main()
{
    stack<char> st;
    char str[50];
    cin>>str;
    cout<<str;
    char *s,x;
    int i=0;
    while(str[i]='\0')
    {
        if(isalnum(str[i]))
            cout<<str[i];
        else if(str[i]=='(')
            st.push(str[i]);
        else if(str[i]==')')
        {
            while(st.top()!='(')
                cout<<st.top();
                st.pop();
        }
        else
        {
            while(precedence(st.top())>=precedence(str[i]))
            {
                cout<<st.top();
                st.pop();
            }
            st.push(str[i]);
        }
        i++;
    }
    cout<<st.size();
    while(st.size()!=0){
        cout<<st.top();
        st.pop();
    }
    return 0;
}