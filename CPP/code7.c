#include<stdio.h>
int main()
{
    int a,b;
    scanf("%d%d",&a,&b);

}


while(true)
{
    int diff = abs(num1-num2),hcf = 1;
    if(num1%diff==0 && num2%dif==0)
        return diff;
    else
    {
        for(int i=2;i<=diff/2;i++)
        {
            if(num1%i==0 && num2%i==0)
                return i;
        }
    }
    return hcf;
}