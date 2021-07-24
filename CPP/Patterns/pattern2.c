#include<stdio.h>
void pattern(int n)
{
    for(int i=1;i<=n;i++)
    {
        for(int j=i;j<=6;j++)
        {
            printf("%d",i);
        }
        printf("\n");
    }
}

int main()
{
    int n;
    scanf("%d",&n);
    pattern(n);
    return 0;
}
/*
4

111111
22222
3333
444
*/