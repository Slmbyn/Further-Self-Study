// function reverseString(str) {
//     const splitStr = (str.split("")).reverse().join('');
//     return splitStr
// }
// // console.log(reverseString("hello"))



// function isPalindrome(str) {
//     const lowerStr = str.toLowerCase();
//     const noComma = lowerStr.replace(/,/g, '').replace(/ /g, '')
//     const reversed = (noComma.split('')).reverse().join('')
//     if (noComma == reversed) {
//         return true
//     } else return false
// }
// // console.log(isPalindrome("A man, a plan, a canal, Panama")); // Output should be true
// // console.log(isPalindrome("race a car")); // Output should be false

// /*
// Write a function fizzBuzz that takes a number as input and returns the following:

// If the number is divisible by 3, return "Fizz".
// If the number is divisible by 5, return "Buzz".
// If the number is divisible by both 3 and 5, return "FizzBuzz".
// Otherwise, return the input number.
// */

// function fizzBuzz(num) {
//     if (num % 3 == 0 && num % 5 != 0) {
//         return 'Fizz'
//     } else if (num % 5 == 0 && num % 3 != 0) {
//         return 'Buzz'
//     } else if (num % 5 == 0 && num % 3 == 0) {
//         return 'FizzBuzz'
//     } else return num
//   }
  
// //   console.log(fizzBuzz(3)); // Output should be "Fizz"
// //   console.log(fizzBuzz(5)); // Output should be "Buzz"
// //   console.log(fizzBuzz(15)); // Output should be "FizzBuzz"
// //   console.log(fizzBuzz(7)); // Output should be 7

// /*
// Problem: Find the Missing Number

// You are given an array of numbers from 1 to N, where one number is missing. 
// Write a function findMissingNumber to find and return the missing number.
// */

// // function findMissingNumber(arr) {
// //     // sort
// //     console.log(`length: ${arr.length}`)
// //     const sortedArr = arr.sort((a,b) => a - b)
// //     // console.log(`sorted: ${sortedArr}`)
// //     // does the value of the next idx equal the value of the last index+1
// //     for(let i = 0; i < sortedArr.length; i++) {
// //         for (let j = 1; j < sortedArr.length; j++) {
// //             if ((sortedArr[i] + 1) != sortedArr[j]) {
// //                 return sortedArr[i] + 1
// //             } else return 'Nothing Missing'
// //         }
// //     }
// // }
// // function findMissingNumber(arr) {
// //     let sum = 0;
// //     for (let i = 0; i < arr.length; i++) {
// //         sum += arr[i]
// //     }
// //     const expectedSum = 0;
// //     for (let i = 1; i < arr.length; i++) {
// //         expectedSum += i;
// //     }
// //     return abs(expectedSum - sum)
// // }

// function findMissingNumber(arr) {
//     const sum = arr.reduce((acc,currentVal) => {
//         return acc + currentVal;
//     }, 0)
//     // compare that with arr.length+1
//     let constArr = [];
//     for(i = 1; i < (arr.length + 2); i++) {
//         constArr.push(i);
//     }
//     const expSum = constArr.reduce((acc, currentVal) => {
//         return acc + currentVal;
//     })
//     return expSum - sum
// }
  
// //   console.log(findMissingNumber([1, 2, 4, 6, 3, 7, 8])); // Output should be 5
// //   console.log(findMissingNumber([1, 3, 4, 5])); // Output should be 2
  

// // Given an array of numbers nums and a target number target,
// // return indices of the two numbers such that they add up to the target.
// // You may assume that each input would have exactly one solution, and you 
// // may not use the same element twice. You can return the answer in any order.

// function twoSum(nums, target) {
//     for (let i = 0; i < nums.length; i++) {
//         for (let j = i + 1; j < nums.length; j++) {
//             console.log(`i=${i} and j=${j}`)
//             if (nums[i] + nums[j] == target) {
//                 return [i,j]
//             }
//         }
//     }
// }

// // console.log(twoSum([2, 7, 11, 15], 9)); // Output should be [0, 1] (nums[0] + nums[1] equals 9)
// // console.log(twoSum([3, 2, 4], 6)); // Output should be [1, 2] (nums[1] + nums[2] equals 6)
// // console.log(twoSum([3, 3], 6)); // Output should be [0, 1] (nums[0] + nums[1] equals 6)

// /*
// Problem: Valid Parentheses

// Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
// determine if the input string is valid.

// An input string is valid if:

// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.
// */

// function isValidParentheses(s) {
//     // 
// }

// // console.log(isValidParentheses("()")); // Output should be true
// // console.log(isValidParentheses("()[]{}")); // Output should be true
// // console.log(isValidParentheses("(]")); // Output should be false
// // console.log(isValidParentheses("([)]")); // Output should be false
// // console.log(isValidParentheses("{[]}")); // Output should be true

// /*
// Problem: Find the Maximum Element

// Write a function findMax that takes an array of 
// numbers as input and returns the maximum element in the array. 
// Do not use built-in functions like Math.max or Array.prototype.reduce.
// */

// function findMax(nums) {
//     let maxNum = 0;
//     for (let i = 0; i < nums.length; i++) {
//         if (nums[i] > maxNum) {
//             maxNum = nums[i];
//         }
//     }
//     return maxNum
// }

// // console.log(findMax([3, 7, 1, 9, 5])); // Output should be 9
// // console.log(findMax([-2, 0, 8, -5])); // Output should be 8

// /*
// Problem: Count Duplicates

// Write a function countDuplicates that takes an array of numbers 
// as input and returns the count of duplicate elements in the array.
// */

// function countDuplicates(nums) {
//     let duplicates = 0;
//     // nested for loops thru nums
//     for ( let i = 0; i < nums.length; i++) {
//         for (let j = i + 1; j < nums.length; j++) {
//             if (nums[i] === nums[j]) {
//                 duplicates++;
//             }
//         }
//     }
//     return duplicates
// }

// // BETTER WAY:

// function countDuplicates(nums) {
//     let duplicates = 0;
//     let counted = [];

//     for (let i = 0; i < nums.length; i++) {
//         for (let j = i + 1; j < nums.length; j++) {
//             if (nums[i] === nums[j] && !counted.includes(nums[i])) {
//                 duplicates++;
//                 counted.push(nums[i]);
//             }
//         }
//     }

//     return duplicates;
// }


// // console.log(countDuplicates([1, 2, 3, 2, 4, 5, 4, 7, 8, 9])); // Output should be 2 (2 and 4 are duplicates)
// // console.log(countDuplicates([3, 7, 1, 9, 5])); // Output should be 0 (no duplicates)
// // console.log(countDuplicates([1, 2, 3, 4, 5])); // Output should be 0 (no duplicates)


// /*
// Problem: Remove Duplicates

// Write a function removeDuplicates that takes an array of 
// numbers as input and returns a new array with duplicate elements removed. 
// The order of elements should be preserved.
// */

// function removeDuplicates(nums) {
//     const numsSet = new Set(nums)
//     const noDuplicates = Array.from(numsSet)
//     return noDuplicates
// }

// //   console.log(removeDuplicates([1, 2, 3, 2, 4, 5, 4, 7, 8, 9])); // Output should be [1, 2, 3, 4, 5, 7, 8, 9]
// //   console.log(removeDuplicates([3, 7, 1, 9, 5])); // Output should be [3, 7, 1, 9, 5] (no duplicates)
// //   console.log(removeDuplicates([1, 2, 3, 4, 5])); // Output should be [1, 2, 3, 4, 5] (no duplicates)

// function returnDuplicates(nums) {
//     let duplicates = [];
//     for (let i = 0; i < nums.length; i++) {
//         for (let j = i + 1; j < nums.length; j++) {
//             if (nums[i] === nums[j] && !duplicates.includes(nums[i])) {
//                 duplicates.push(nums[i]);
//             }
//         }
//     }
//     return duplicates
// }

// // ALTERNATIVE WAY USING SET:

// function returnDuplicatesWithSet(nums) {
//     const duplicatesSet = new Set();
    
//     for (let i = 0; i < nums.length; i++) {
//         for (let j = i + 1; j < nums.length; j++) {
//             if (nums[i] === nums[j]) {
//                 duplicatesSet.add(nums[i]);
//             }
//         }
//     }
//     return Array.from(duplicatesSet);
// }


// // console.log(returnDuplicates([1, 2, 3, 2, 4, 5, 4, 7, 8, 9])); // Output should be 2 (2 and 4 are duplicates)
// // console.log(returnDuplicates([3, 7, 1, 9, 5])); // Output should be 0 (no duplicates)
// // console.log(returnDuplicates([1, 2, 3, 4, 5])); // Output should be 0 (no duplicates)

// /*
// Problem: Rotate Array

// Write a function rotateArray that takes an array of numbers and 
// a number k as input and rotates the array to the right by k steps.

// For example, if the input array is [1, 2, 3, 4, 5] and k is 2, the output should be [4, 5, 1, 2, 3].
// */

// function rotateArray(nums, k) {
//     if (k != 0 && k < nums.length){
//         const sliced = nums.slice(k + 1,nums.length)
//         const shiftedArray = nums.unshift(sliced)
//         const flatNums = nums.flat()
//         // remove sliced elements
        
//         return flatNums
//     }
// }
  
// //   console.log(rotateArray([1, 2, 3, 4, 5], 2)); // Output should be [4, 5, 1, 2, 3]
// //   console.log(rotateArray([3, 7, 1, 9, 5], 3)); // Output should be [1, 9, 5, 3, 7]


// /*
// Problem: Sum of Two

// Write a function sumOfTwo that takes two arrays of numbers 
// and a target number as input and returns true if there exist 
// two numbers, one from each array, that add up to the target number. 
// Otherwise, return false.
// */

// function sumOfTwo(nums1, nums2, target) {
//     for ( let i = 0; i < nums1.length; i++) {
//         for( let j = 0; j < nums2.length; j++) {
//             if (nums1[i] + nums2[j] == target) {
//                 return true
//             }
//         }
//     } return false
// }

//   console.log(sumOfTwo([1, 2, 3], [4, 5, 6], 8)); // Output should be true (3 + 5 = 8)
//   console.log(sumOfTwo([1, 2, 3], [4, 5, 6], 12)); // Output should be false (no pair adds up to 12)



//   let leftArr = [];
//   let rightArr = [];
//   // remove all -1
//   const nonNegArr = arr.filter(item => item !== -1);
//   // loop thru nonNegArr and push alternating values into each arrays starting at index 1
//   for (let i=1; i < nonNegArr.length; i++) {
//        // even index numbers go right
//       if ( i % 2 === 0) {
//           rightArr.push(nonNegArr[i]);
//       } else {
//           leftArr.push(nonNegArr[i]);
//       }
//   }
//   // sum each and return left/right
//   const leftSum = leftArr.reduce((acc, curr) => acc + curr, 0);
//   const rightSum = rightArr.reduce((acc, curr) => acc + curr, 0)
//   if (leftSum > rightSum) {
//       return 'Left';
//   } else if(leftSum < rightSum) {
//       return 'Right';
//   } else {
//       return "";
//   }




const solution = (array) => {
    function merge(left, right) {
        let merged = [];
        let i = 0;
        let j = 0;

        while (i < left.length && j < right.length) {
            if (left[i] < right[j]) {
                merged.push(left[i++]);
            } else {
                merged.push(right[j++]);
            }
        }

        while (i < left.length) {
            merged.push(left[i++]);
        }

        while (j < right.length) {
            merged.push(right[j++]);
        }

        return merged;
    }

    function mergeSort(array) {
        if (array.length <= 1) {
            return array;
        }

        let middleIndex = Math.floor(array.length / 2);

        let left = array.slice(0, middleIndex);
        let right = array.slice(middleIndex, array.length);
        return merge(mergeSort(left), mergeSort(right));
    }

    return mergeSort(array);
};

const input1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5];
// console.log(solution(input1));

const input2 = [8, 4, 2, 7, 1, 9, 5, 3, 6];
// console.log(solution(input2));

const input3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1];
// console.log(solution(input3));

const input4 = [2, 3, 1, 4, 5];
// console.log(solution(input4));


function reverseTheString(string) {
    let newString = '';
    for ( let i = 0; i < string.length; i++ ) {
        
    }
}

function average(list) {
    const length = list.length
    const sum = list.reduce((a,b) => a + b)
    return sum / length
}

// console.log(average([1, 2, 3, 4, 5]))

