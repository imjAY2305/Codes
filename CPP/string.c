#include<stdio.h>
int main()
{
    char greet[] = "Hello";
    char greet1[] = {'h','e','l','l','o','\0'};
    printf("%s",greet);
    printf("\n%s",greet1);
    return 0;
}

/*
String functions

strcpy(s1,s2) -> s1 copied to s2
strcat(s1,s2) -> s2 concatenated at the end of s1
strlen(s1) -> returns length of string
strcmp(s1,s2) -> compares two strings
strchr(s1,ch) -> returns pointer at first occurence of ch in s1

*/