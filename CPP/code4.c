#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main()
{
    char str[100],res[100];
    gets(str);
    for(int i=0;str[i]!='\0';i++)
    {
        if(str[i]==' ')
            printf("$");
        else
            printf("%c",str[i]);
    }
    return 0;
}