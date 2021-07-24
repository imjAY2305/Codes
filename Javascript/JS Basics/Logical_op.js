let isGuestOneVegan = true
let isGuestTwovegan = false

if(isGuestOneVegan && isGuestTwovegan)
    console.log("Only offer vegan dishes")
else if(isGuestTwovegan || isGuestOneVegan)
    console.log("Offer some Vegan options")
else
    console.log("Offer everything")