let sample = function(a,b,c)
{
    x = a+b
    if(c=='+')
        return a+b
    else if(c=='-')
        return a-b
    else
        return "Enter valid operator"
}

let res = sample(10,3,'1')
console.log(res)
console.log(x)