#include<stdio.h>
int main()
{
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n*2;i+=2)
    {
        for(int j=1;j<=i;j++)
        {
            printf("%d ",j);
        }
        printf("\n");
    }
    for(int i=n*2-2;i>=1;i-=2)
    {
        for(int j=1;j<i;j++)
        {
            printf("%d ",j);
        }
        printf("\n");
    }
    return 0;
}