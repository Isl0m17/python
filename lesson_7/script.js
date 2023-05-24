'use strict'
let number = +(prompt("Enter the number"))

function checkTheNumber(){
    if (number % 2 == 0){
        console.log("The number is even")
    }
    else{
        console.log("The number is odd")
    }
}
checkTheNumber()