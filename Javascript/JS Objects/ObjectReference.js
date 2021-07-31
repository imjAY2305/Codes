let myAccount = {
    ID : "imjAY",
    password : "Lokanath@121",
    balance : 20000
}

let Operation = function(acc, amount, op){
    if(op=="W")
        acc.balance -= amount
    if(op=="D")
        acc.balance += amount
}

Operation(myAccount,500,"D")
console.log(myAccount)
Operation(myAccount,2000,"W")
console.log(myAccount)