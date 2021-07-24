#include<stdio.h>
int main()
{
    char str[100];
    gets(str);
    int a=0,d=0,ot=0,i=0;
    while(str[i]!='\0'){
        if((str[i]>='a' && str[i]<='z') || (str[i]>='A' && str[i]<='Z'))
        {
            a++;
        }
        else if(str[i]>='0' && str[i]<='9')
        {
            d++;
        }
        else
        {
            ot++;
        }
        i++;
    }
    printf("%d %d %d",a,d,ot);
    return 0;
}