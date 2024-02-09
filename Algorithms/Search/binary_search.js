const array = [5,3,6,2,1,9,15,4]

function search (arr, x) {
    const sortedArr = arr.sort((a,b) => a - b);
    const highIdx = arr.length - 1;
    const result = binarySearch(sortedArr, 0 , highIdx, x);
    if (result == -1) {
        return 'Element not found'
    }
    return `Element found at index ${result}`
}

function binarySearch (arr, low, high, x) {
    if (high >= low) {
        // if (high % 2 != 0) {
            const mid = low + (high - low)/2;
            if(arr[mid] == x) {
                return mid;
            }
            if (arr[mid] > x) {
                return binarySearch(arr, low, mid-1, x);
            }
            return binarySearch(arr, mid+1, high, x)
        // }
    return -1;
    }
}

console.log(search(array, 6))











// function binarySearch (arr, num) {
    // sort the array
    // calculate a midpoint index
    // if (arr.length() % 2 != 0)
        // const midpointIndex = 0 + (((arr.length() - 1) - 0)/2)
    // const midpointValue = arr[midpointIndex];
    // check if desired num is equal to the midpointValue
    // check if desired num is higher/lower than midpointValue
    // if higher: 
        // store the higher half of the array in a variable
        // recursivley call binarySearch function and pass the new array into it
        // OR: just for-loop thru the higher half and look for the num
        // if lower:
        // store the lower half of the array in a variable
        // recursivley call binarySearch function and pass the new array into it
        // OR: just for-loop thru the lower half and look for the num
// }

