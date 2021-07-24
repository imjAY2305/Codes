#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main()
{
    char str[100],rev[100];
    gets(str);
    int n = strlen(str);
    int index, start, end,i;
    index = 0;
    start = n-1;
    end = n-1;
    while(start>0)
    {
        if(str[start]==' ')
        {
            i = start+1;
            while(i<=end)
            {
                rev[index] = str[i];
                i++;
                index++; 
            }
            rev[index++]=' ';
            end = start-1;
        }
        start--;
    }
    for(int i=0;i<=end;i++)
    {
        rev[index] = str[i];
        index++;
    }
    rev[index] = '\0';
    printf("%s",rev);
    return 0;
}