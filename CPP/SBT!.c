//GRADES

#include<stdio.h>
char checkGrade(int score)
{
if(score<=60)
return 'D';
else if((61<=score)&&(score<=75))
return 'C';
else if((76<=score)&&(score<=90))
return 'B';
else
return 'A';
}
int main()
{
 int score;
 scanf("%d",&score);
 printf("%c\n",checkGrade(score));
}

//SERIES

 #include<stdio.h>
int main()
{
 int b=34,n,i;
 scanf("%d",&n);
 printf("%d ",b);
 for(i=1;i<n;i++)//error
{
 b=(b/2)+1;
 printf("%d ",b);

 }
return 0;
}

//MULTIPLICATION TABLE

#include "stdio.h"
void printTable(int n);

int main(){
int n;
scanf("%d",&n);
printTable(n);
}
void printTable(int num)
{
int i,value;

for(i=1;i<=10;i++){//error
value = num*i ;//error

printf("%d\n", value);
}
}
