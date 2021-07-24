#include<stdio.h>
int main()
{
    int n;
    scanf("%d",&n);
    int e=0,o=0;
    int even[n],odd[n];
    int arr[n];
    for(int i=0;i<n;i++){
        int x;
        scanf("%d",&x);
        if(x%2==0)
            even[e++] = x;
        else
            odd[o++] = x;
    }
    int temp;
    for(int i=0;i<e;i++)
    {
        for(int j=i+1;j<e;j++)
        {
            if(even[i]>even[j]){
                temp = even[i];
                even[i] = even[j];
                even[j] = temp;
            }
        }
    }
    for(int i=0;i<o;i++)
    {
        for(int j=i+1;j<o;j++)
        {
            if(odd[i]>odd[j]){
                temp = odd[i];
                odd[i] = odd[j];
                odd[j] = temp;
            }
        }
    }
    int c=0,b=0;
    for(int i=0;i<e+o;i++)
    {
        if(i<e)
            printf("%d ",even[c++]);
        else
            printf("%d ",odd[b++]);
    }
    return 0;
}