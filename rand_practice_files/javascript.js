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
// console.log(isPalindrome("A man, a plan, a canal, Panama")); // Output should be true
// console.log(isPalindrome("race a car")); // Output should be false

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
  
//   console.log(fizzBuzz(3)); // Output should be "Fizz"
//   console.log(fizzBuzz(5)); // Output should be "Buzz"
//   console.log(fizzBuzz(15)); // Output should be "FizzBuzz"
//   console.log(fizzBuzz(7)); // Output should be 7

/*
Problem: Find the Missing Number

You are given an array of numbers from 1 to N, where one number is missing. 
Write a function findMissingNumber to find and return the missing number.
*/

// function findMissingNumber(arr) {
//     // sort
//     console.log(`length: ${arr.length}`)
//     const sortedArr = arr.sort((a,b) => a - b)
//     // console.log(`sorted: ${sortedArr}`)
//     // does the value of the next idx equal the value of the last index+1
//     for(let i = 0; i < sortedArr.length; i++) {
//         for (let j = 1; j < sortedArr.length; j++) {
//             if ((sortedArr[i] + 1) != sortedArr[j]) {
//                 return sortedArr[i] + 1
//             } else return 'Nothing Missing'
//         }
//     }
// }
// function findMissingNumber(arr) {
//     let sum = 0;
//     for (let i = 0; i < arr.length; i++) {
//         sum += arr[i]
//     }
//     const expectedSum = 0;
//     for (let i = 1; i < arr.length; i++) {
//         expectedSum += i;
//     }
//     return abs(expectedSum - sum)
// }

function findMissingNumber(arr) {
    const sum = arr.reduce((acc,currentVal) => {
        return acc + currentVal;
    }, 0)
    // compare that with arr.length+1
    let constArr = [];
    for(i = 1; i < (arr.length + 2); i++) {
        constArr.push(i);
    }
    const expSum = constArr.reduce((acc, currentVal) => {
        return acc + currentVal;
    })
    return expSum - sum
}
  
//   console.log(findMissingNumber([1, 2, 4, 6, 3, 7, 8])); // Output should be 5
//   console.log(findMissingNumber([1, 3, 4, 5])); // Output should be 2
  

// Given an array of numbers nums and a target number target,
// return indices of the two numbers such that they add up to the target.
// You may assume that each input would have exactly one solution, and you 
// may not use the same element twice. You can return the answer in any order.

function twoSum(nums, target) {
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            console.log(`i=${i} and j=${j}`)
            if (nums[i] + nums[j] == target) {
                return [i,j]
            }
        }
    }
}

console.log(twoSum([2, 7, 11, 15], 9)); // Output should be [0, 1] (nums[0] + nums[1] equals 9)
console.log(twoSum([3, 2, 4], 6)); // Output should be [1, 2] (nums[1] + nums[2] equals 6)
console.log(twoSum([3, 3], 6)); // Output should be [0, 1] (nums[0] + nums[1] equals 6)







