#include<bits/stdc++.h>
using namespace std;
void print(stack<int> st)
{
    while(st.size()>0){
        cout<<st.top()<<endl;
        st.pop();
    }
}
int main()
{
    stack<int> st;
    /*push 1,2,3,4,5*/
    for(int i=1;i<=5;i++)
        st.push(i);
    print(st);
    return 0;
}