let mybook = {
    title : "JavaScript",
    year : 2000,
    price : "451/-"
}

let mybook1 = {
    title : "C/C++",
    year : "2006",
    price : "200/-"
}

let display = function(obj){
    console.log(obj)
}

display(mybook)
display(mybook1)

// We can use objects concept to return multiple values from a function.
// Example is shown below.

let sample = function(a,b){
    return {
        1 : a,
        2 : b
    }
}

let res = sample(5,6)
console.log(res)