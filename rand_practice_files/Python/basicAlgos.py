#*************************************************** MERGE SORT
def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: If the array has 0 or 1 elements, it is already sorted

    # Divide the array into two halves
    mid = len(arr) // 2
    left_subarray = arr[:mid]
    right_subarray = arr[mid:]

    # Recursively sort each half
    left_sorted = merge_sort(left_subarray)
    right_sorted = merge_sort(right_subarray)

    # print('left_sorted:', left_sorted)
    # print('right_sorted:', right_sorted)
    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    merged = []
    left_index = right_index = 0

    # Compare elements from the left and right halves and merge them in sorted order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append any remaining elements from the left and right halves
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = merge_sort(my_list)

#*********************************************** SLIDING WINDOW
def slide(arr,k):
    sum = 0
    max_sum = sum
# sum of first 3
    for i in range(k):
        sum += arr[i]

    for i in range(len(arr) - k):
        sum -= arr[i]
        sum += arr[i+k]
        
        max_sum = max(max_sum, sum)
        
    return max_sum

# Other way
def sliding_window(arr, k):
    max_sum = float('-inf')  # Initialize max_sum to negative infinity
    window_sum = 0  # Initialize the sum of current window

    # Iterate through the array, sliding the window
    for i in range(len(arr)):
        temp = arr[i]
        # Add the element at the right end of the window
        window_sum += arr[i]
        
        # If we've reached the size k, update max_sum and move the window
        if i >= k - 1:
            max_sum = max(max_sum, window_sum)  # Update max_sum
            # Subtract the element at the left end of the window
            window_sum -= arr[i - (k - 1)]

    return max_sum

#************************************************* BINARY SEARCH
def do_binary(arr, target):
    n = len(arr)
    
    mid = n // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return do_binary(arr[mid:], target)
    elif arr[mid] > target:
        return do_binary(arr[:mid], target)
    return -1

# other way
def binary_search(arr, target):
    left = 0
    right =len(arr) - 1  # Initialize left and right pointers
    
    while left <= right:
        mid = (left + right) // 2  # Calculate the middle index
        
        if arr[mid] == target:
            return mid  # Return the index if the target is found
        
        elif arr[mid] < target:
            left = mid + 1  # Move the left pointer to the right half
            
        else:
            right = mid - 1  # Move the right pointer to the left half
            
    return -1  # Return -1 if the target is not found

# Example usage:
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 11
index = binary_search(arr, target)
if index != -1:
    print("Target", target, "found at index", index)
else:
    print("Target", target, "not found in the array")

#************************************************* TWO POINTER

def two_sum(arr, target):
    left, right = 0, len(arr) - 1  # Initialize left and right pointers
    
    while left < right:
        current_sum = arr[left] + arr[right]  # Calculate the sum of elements at left and right pointers
        
        if current_sum == target:
            return [left, right]  # Return the indices if the sum equals the target
        
        elif current_sum < target:
            left += 1  # Move the left pointer to the right to increase the sum
            
        else:
            right -= 1  # Move the right pointer to the left to decrease the sum
            
    return None  # Return None if no such pair exists

# Example usage:
arr = [-2, 1, 2, 4, 7, 11]
target = 13
indices = two_sum(arr, target)
if indices:
    print("Indices of elements adding up to", target, ":", indices)
else:
    print("No pair of elements found adding up to", target)

#************************************************** GREEDY ALGO
def min_coins(coins, amount):
    coins.sort(reverse=True)  # Sort the coins in descending order
    num_coins = 0  # Initialize the count of coins needed
    
    for coin in coins:
        while amount >= coin:  # Greedily choose the largest coin denomination possible
            num_coins += 1
            amount -= coin
    
    return num_coins if amount == 0 else -1  # Return -1 if exact change cannot be made

# Example usage:
coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]  # Available coin denominations
amount = 93
min_coins_needed = min_coins(coins, amount)
if min_coins_needed != -1:
    print("Minimum number of coins needed for", amount, "cents:", min_coins_needed)
else:
    print("Exact change cannot be made for", amount, "cents using the given denominations")

#************************************************** BUBBLE SORT
def bubble_sort(arr):
    n = len(arr)  # Get the length of the array
    for i in range(n):  # Iterate through each element of the array
        # Last i elements are already in place, so we don't need to check them again
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print("Sorted array:", my_list)

#*************************************************** HASH MAP
mapped = {}
def mapped_recursive_factorial(n):
    if n <= 1:
        return 1
    if n in mapped:
        return mapped[n]
    mapped[n] = n * mapped_recursive_factorial(n-1)
    return mapped[n]

#other way
def two_sum_indices(nums, target):
    # Create a dictionary to store the index of each number
    num_to_index = {}
    
    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in num_to_index:
            # If found, return the indices of the two numbers
            return [num_to_index[complement], i]
        
        # Otherwise, add the current number and its index to the dictionary
        num_to_index[num] = i
    
    # Return None if no such pair exists
    return None

# Example usage:
nums = [2, 7, 11, 15]
target = 9
indices = two_sum_indices(nums, target)
if indices:
    print("Indices of numbers adding up to", target, ":", indices)
else:
    print("No pair of numbers found adding up to", target)

#****************************************** DYNAMIC PROGRAMMING
def fibonacci(n):
    # Base cases: fibonacci(0) = 0, fibonacci(1) = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Initialize an array to store fibonacci numbers
    fib = [0] * (n + 1)
    fib[1] = 1  # fibonacci(1) is 1
    
    # Calculate fibonacci numbers using dynamic programming
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib[n]

# Example usage:
n = 10
result = fibonacci(n)
print("Fibonacci number at index", n, ":", result)

#****************************************************** RECURSIVE
def fibonacci(n):
    # Base cases: fibonacci(0) = 0, fibonacci(1) = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Recursive call to calculate Fibonacci number
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage:
n = 10
result = fibonacci(n)
print("Fibonacci number at index", n, ":", result)


#************************************************** BACKTRACKING
def permute(nums):
    result = []  # Initialize the list to store permutations
    
    def backtrack(current_permutation):
        if len(current_permutation) == len(nums):
            result.append(current_permutation[:])  # Add a copy of the current permutation to the result
            return
        
        for num in nums:
            if num not in current_permutation:
                current_permutation.append(num)  # Choose
                backtrack(current_permutation)  # Explore
                current_permutation.pop()  # Unchoose
    
    backtrack([])
    return result

# Example usage:
nums = [1, 2, 3]
permutations = permute(nums)
print("All permutations of", nums, ":", permutations)



#******************************************* DIVIDE AND CONQUER
def max_crossing_subarray(arr, low, mid, high):
    left_sum = float('-inf')  # Initialize the sum of the left subarray as negative infinity
    sum = 0  # Initialize a variable to store the sum of elements
    max_left = mid  # Initialize the index of the maximum sum subarray on the left side as mid
    
    # Calculate the maximum sum of the left subarray
    for i in range(mid, low - 1, -1):  # Traverse the array from mid to low
        sum += arr[i]  # Add the current element to the sum
        if sum > left_sum:  # If the current sum is greater than the left_sum
            left_sum = sum  # Update the left_sum
            max_left = i  # Update the index of the maximum sum subarray
    
    right_sum = float('-inf')  # Initialize the sum of the right subarray as negative infinity
    sum = 0  # Reset the sum variable
    max_right = mid + 1  # Initialize the index of the maximum sum subarray on the right side as mid + 1
    
    # Calculate the maximum sum of the right subarray
    for j in range(mid + 1, high + 1):  # Traverse the array from mid + 1 to high
        sum += arr[j]  # Add the current element to the sum
        if sum > right_sum:  # If the current sum is greater than the right_sum
            right_sum = sum  # Update the right_sum
            max_right = j  # Update the index of the maximum sum subarray
    
    # Return the indices and the sum of the maximum subarray crossing the midpoint
    return (max_left, max_right, left_sum + right_sum)

def max_subarray(arr, low, high):
    if low == high:  # Base case: Only one element in the array
        return (low, high, arr[low])  # Return the index and value of the single element
    else:
        mid = (low + high) // 2  # Calculate the midpoint of the array
        # Recursive calls to find the maximum subarrays in the left and right halves
        left_low, left_high, left_sum = max_subarray(arr, low, mid)
        right_low, right_high, right_sum = max_subarray(arr, mid + 1, high)
        cross_low, cross_high, cross_sum = max_crossing_subarray(arr, low, mid, high)
        
        # Compare the maximum subarray sums of the left, right, and crossing subarrays
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)  # Return the left subarray
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)  # Return the right subarray
        else:
            return (cross_low, cross_high, cross_sum)  # Return the crossing subarray

# Example usage:
arr = [2, -4, 1, 9, -6, 7, -3]
low, high, max_sum = max_subarray(arr, 0, len(arr) - 1)
print("Maximum subarray sum:", max_sum)
print("Indices of the maximum subarray:", low, "to", high)
