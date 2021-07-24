#include<stdio.h>
int f(int x,int y)
{
    if(x==y)
        return 0;
    else if(x%5==0 && y%5==0)
        return x<y?x:y;
    else
        return x>y?x:y;
}
int main()
{
    int a,b;
    scanf("%d%d",&a,&b);
    printf("%d",f(a,b));
    return 0;
}