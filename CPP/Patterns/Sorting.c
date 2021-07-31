#include<stdio.h>
int main()
{
    int n;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++)
        scanf("%d",&arr[i]);
    int temp;
    for(int i=0;i<n;i++) //PASS
    {
        for(int j=0;j<n;j++) //CHECKING
        {
            if(arr[j]>arr[j+1])
            {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
    for(int i=0;i<n;i++)
        printf("%d ",arr[i]);
    return 0;
}