#include<stdio.h>
#include<stdlib.h>
int main()
{
    char str[100];
    scanf("%s",&str);
    int n = strlen(str);
    int flag = 1;
    for(int i=0;i<n;i++)
    {
        if(str[i]!=str[n-i-1])
        {
            flag = 0;
            break;
        }
    }
    if(flag)
        printf("PALINDROME");
    else    
        printf("NOT PALINDROME");
    return 0;
}