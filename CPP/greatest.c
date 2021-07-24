int greatest(int a,int b,int c)
{
    if(a>b && a>c)
        return a;
    else if(b>c && b>a)
        return b;
    else    
        return c;
}

int great(int a,int b,int c)
{
    return (a>b)?((a>c)?a:b):((b>c)?b:c);
}