#include<stdio.h>
#include<math.h>
#include<string.h>
int main()
{
    int a,b;
    scanf("%d%d",&a,&b);
    a = abs(a);
    b = abs(b);
    int temp =b;
    while(temp>0)
    {
        a *= 10;
        temp = temp/10;
    }
    printf("%d",a+b);
    return 0;
}
