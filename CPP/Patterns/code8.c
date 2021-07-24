#include<stdio.h>
int f(int x,int y)
{
    if(x>13 && y>13)
        return 0;
    else if(x>13 && y<=13)
        return y;
    else if(x<13 && y>13)
        return x;
    return x>y?x:y;
}
int main()
{
    int a,b;
    scanf("%d%d",&a,&b);
    printf("%d",f(a,b));
    return 0;
}