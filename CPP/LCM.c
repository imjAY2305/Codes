#include<stdio.h>
int main()
{
    int a,b,lcm,ref=2;
    scanf("%d%d",&a,&b);
    lcm = (a>b)?a:b;
    while(1)
    {
        if(lcm%a==0 && lcm%b==0)
        {
            printf("%d",lcm);
            break;
        }
        else
        {
            lcm *= ref;
            ref++;
        }    
    }
    return 0;
}