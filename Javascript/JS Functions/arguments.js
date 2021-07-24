let sample = function(a,b,c=3)
{
    return a*b*c
}

let res = sample(3,4)
console.log(res)

//Challenge

let getTip = function(amount=0,percent=0)
{
    return (amount/100)*percent
}

let amount = 430
let percent = 8
let res1 = getTip(amount,percent)
console.log("The tip amount is : ",res1)