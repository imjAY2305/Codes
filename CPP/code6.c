//Encrypt
#include<stdio.h>
#include<stdlib.h>
int main()
{
    int n;
    scanf("%d",&n);
    int unit = n%10;
    int ten = (n/10)%10;
    int res = (n/10)*10+abs(unit-ten);
    printf("%d",res);
    return 0;
}