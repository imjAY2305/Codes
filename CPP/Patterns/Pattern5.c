#include<stdio.h>
int main()
{
    int n,c;
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
        c = i;
        for(int j=1;j<=n;j++)
        {
            if(j<=n-i)
                printf(" ");
            else
                printf("%d",c--);
        }
        printf("\n");
    }
}