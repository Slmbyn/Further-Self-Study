function reverseString(str) {
    const splitStr = (str.split("")).reverse().join('');
    return splitStr
}


// console.log(reverseString("hello"))



function isPalindrome(str) {
    const lowerStr = str.toLowerCase();
    const noComma = lowerStr.replace(/,/g, '').replace(/ /g, '')
    const reversed = (noComma.split('')).reverse().join('')
    if (noComma == reversed) {
        return true
    } else return false
}

console.log(isPalindrome("A man, a plan, a canal, Panama")); // Output should be true
console.log(isPalindrome("race a car")); // Output should be false

/*
Write a function fizzBuzz that takes a number as input and returns the following:

If the number is divisible by 3, return "Fizz".
If the number is divisible by 5, return "Buzz".
If the number is divisible by both 3 and 5, return "FizzBuzz".
Otherwise, return the input number.
*/

function fizzBuzz(num) {
    if (num % 3 == 0 && num % 5 != 0) {
        return 'Fizz'
    } else if (num % 5 == 0 && num % 3 != 0) {
        return 'Buzz'
    } else if (num % 5 == 0 && num % 3 == 0) {
        return 'FizzBuzz'
    } else return num
  }
  
  console.log(fizzBuzz(3)); // Output should be "Fizz"
  console.log(fizzBuzz(5)); // Output should be "Buzz"
  console.log(fizzBuzz(15)); // Output should be "FizzBuzz"
  console.log(fizzBuzz(7)); // Output should be 7
  







