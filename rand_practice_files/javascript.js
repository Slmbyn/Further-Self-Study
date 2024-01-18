// function reverseString(str) {
//     const splitStr = (str.split("")).reverse().join('');
//     return splitStr
// }


// console.log(reverseString("hello"))



function isPalindrome(str) {
    // make str lowercase
    const lowerStr = str.toLowerCase();
    // find and remove all commas and spaces
    const noComma = lowerStr.replace(/,/g, '').replace(/ /g, '') // the str with no commas, no space, no caps
    console.log(`noComma: ${noComma}`)
    // split it (will now be an array) // reverse it & join it (back into a string)
    const reversed = (noComma.split('')).reverse().join('') // reversed version of noComma
    console.log(`reversed: ${reversed}`)
    if (noComma == reversed) {
        return true
    } else return false
}

console.log(isPalindrome("A man, a plan, a canal, Panama")); // Output should be true
console.log(isPalindrome("race a car")); // Output should be false