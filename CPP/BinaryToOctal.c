#include<stdio.h>
int toOctal(long long int bin)
{
    int dec=0,oct=0,i=1;
    //Binary to Decimal
    while(bin!=0)
    {
        dec += (bin%10)*i;
        i *= 2;
        bin /= 10;
    }
    //Decimal to Octal
    i = 1;
    while(dec!=0)
    {
        oct += (dec%8)*i;
        i *= 10;
        dec /= 8;
    }
    return oct;
}
int main()
{
    long long int num;
    int res;
    scanf("%lld",&num);
    res = toOctal(num);
    printf("%d",res);
    return 0;
}