#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main()
{
    char a[20],b[20];
    scanf("%s%s",&a,&b);
    int arr[3],brr[3],x=0,y=0;
    char ref1[20],ref2[20];
    for(int i=0;i<strlen(a);i++)
    {
        if(a[i]!=':')
        {
            strcat(ref1,a[i]);
            strcat(ref2,b[i]);
        }
        else{
            arr[x++] = atoi(ref1);
            brr[y++] = atoi(ref2);
            ref1 = "";
            ref2 = "";
            printf("1");
        }
        printf("%s %s",ref1,ref2);
    }
    printf("\n%d %d\n",x,y);
    for(int i=0;i<x;i++)
        printf("%d %d",arr[i],brr[i]);
    return 0;
}