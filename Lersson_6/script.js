'use strict'

let stringForExperiment = "string for experiment"

console.log(stringForExperiment)
console.log(typeof(stringForExperiment))
console.log(stringForExperiment.length)
console.log(stringForExperiment.slice(0, 10))

stringForExperiment = stringForExperiment.replace("s", "s")
stringForExperiment = stringForExperiment.replaceAll("s", "s")

console.log((stringForExperiment))

let smallletters = "abcdsefg"
let bigletters = "ABCDERFG"

console.log(smallletters)
console.log(smallletters.toUpperCase())
console.log(bigletters.toLowerCase())

let stringFromUser = prompt()

console.log(stringFromUser)
console.log(stringFromUser.trim())

let string = "123456789"

console.log(string.charAt(2))
console.log(string[2])
