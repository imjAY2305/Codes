let calci = function(marks,total)
{
    let res = (marks/total)*100
    if(res>=90)
        return `Your Grade is "O", with a score of ${res}%`
    else if(res>=80)
        return `Your Grade is "A", with a score of ${res}%`
    else if(res>=70)
        return `Your Grade is "B", with a score of ${res}%`
    else if(res>=60)
        return `Your Grade is "C", with a score of ${res}%`
    else if(res>=50)
        return `Your Grade is "D", with a score of ${res}%`
    else
        return `Sorry, You have failed this year, Better luck next time!`
}

let marks = 15
let total = 30
let ans = calci(marks,total)
console.log(ans)