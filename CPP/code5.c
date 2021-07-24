#include<stdio.h>
int main()
{
    int s,n,e;
    scanf("%d%d%d",&s,&n,&e);
    int temp = s;
    for(int i=0;i<n;i++)
    {
        printf("%d ",s);
        if(s<e)
            s++;
        else    
            s = temp;
    }
    return 0;
}