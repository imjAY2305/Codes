#include<stdio.h>
void pattern(int n)
{
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
            printf("%d",i);
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
1111
2222
3333
4444
*/