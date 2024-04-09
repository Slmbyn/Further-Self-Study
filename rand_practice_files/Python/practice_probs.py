import time
from memory_profiler import profile

# # sum of 2 digits
# def sum_of_two (a, b):
#     return a + b

# print(sum_of_two(1,3))

def shuffle(nums, n):
    first_half = nums[:n]
    second_half = nums[n:]
    shuffled = []
    for i in range(n):
        shuffled.append(first_half[i])
        shuffled.append(second_half[i])
    print(shuffled)
    return shuffled

    # zipped = list(zip(first_half, second_half))
    # # result = list(zipped)
    # print(zipped)
    # # return zipped

# shuffle([1,2,3,4,4,3,2,1], 4)
from functools import reduce
def maxSubArray(nums):
    subarrays_sum = []
    max_num = subarrays_sum[0]
    for start in range(len(nums)):
        for end in range(start +1, len(nums)+1):
            subarray = nums[start:end]
            subarray_sum = reduce(subarray, sum)
            subarrays_sum.append(subarray_sum)
    # def find_max(subarrays_sum):
    for num in subarrays_sum:
        if num > max_num:
            max_num = num
    return max_num

# print(maxSubArray([-64,78,56,10,-8,26,-18,47,-31,75,89,13,48,-19,-69,36,-39,55,-5,-4,-15,-37,-27,-8,-5,35,-51,83,21,-47,46,33,-91,-21,-57,0,81,1,-75,-50,-23,-86,39,-98,-29,69,38,32,24,-90,-95,86,-27,-23,-22,44,-88,3,27,9,55,-50,-80,40,5,-61,-82,-14,40,-58,35,93,-68,-26,94,3,-79,9,-88,21,19,-84,7,91,-8,84,12,-19,-13,-83,66,-80,-34,62,59,48,-98,53,-66,18,94,46,11,-73,96,-18,6,-83,91,17,38,10,9,-78,-22,77,83,89,-42,-30,-94,-98,-34,-51,63,-97,96,64,55,-93,-41,27,52,69,53,26,-71,-64,42,-80,52,-43,6,-62,-21,83,-85,-38,49,-50,8,55,-72,74,80,90,53,53,32,-15,36,90,-88,-34,37,41,91,65,76,33,61,5,90,-33,42,-54,-73,34,-16,75,83,91,7,-89,42,-36,77,-5,-83,9,80,53,-23,68,-81,90,10,-90,55,-14,19,-7,91,-14,59,33,31,62,-33,-85,37,-73,83,-78,-86,25,-15,91,97,2,-23,54,-68,53,22,-73,43,-68,-87,-25,18,31,67,-14,94,3,-81,25,-35,-37,17,79,-34,-23,-99,-43,-98,-38,-52,75,63,1,29,71,-68,-71,74,51,-40,86,-73,54,-5,70,-60,-11,-49,-64,90,-8,-25,-16,-52,40,60,-75,96,39,-13,-79,14,-73,22,-79,75,30,-51,49,-19,-15,36,-16,-60,-69,-68,-21,-4,-18,-9,-14,50,65,70,75,-17,30,99,-44,-31,-14,-46,60,-10,52,80,-35,-18,-94,-86,62,-10,49,-53,6,56,-45,62,-48,36,-47,15,-37,-81,-15,-62,-22,91,-85,33,-62,-23,86,97,66,15,54,-69,96,36,-55,36,-97,70,82,9,4,-63,-29,32,49,23,-53,88,18,8,-96,72,-23,-82,6,14,-6,-31,-12,-39,61,-58,-32,57,77,12,-7,56,-40,-48,-35,40,-35,12,-28,90,-87,-4,79,30,80,82,-20,-43,76,62,70,-30,-92,-42,7,68,-24,75,26,-70,-36,95,86,0,-52,-49,-60,12,63,-11,-20,75,84,-41,-18,41,-82,61,98,70,0,45,-83,8,-96,24,-24,-44,-24,-98,-14,39,97,-51,-60,-78,-24,-44,10,-84,44,89,67,5,-75,-73,-53,-81,64,-55,88,-35,89,-94,72,69,29,-52,-97,81,-73,-35,20,-99,13,36,98,65,69,8,81,13,-25,25,95,-1,51,-58,-5,16,-37,-17,57,-71,-35,29,75,70,53,77,51,79,-58,-51,56,31,84,54,-27,30,-37,-46,-56,14,56,-84,89,7,-43,-16,99,19,67,56,24,-68,-38,-1,-97,-84,-24,53,71,-6,-98,28,-98,63,-18,-25,-7,21,5,13,-88,-39,28,-98,68,61,-15,44,-43,-71,1,81,-39,62,-20,-60,54,33,69,26,-96,48,-69,-94,11,-11,-20,80,87,61,-29,98,-77,75,99,67,37,-38,11,93,-10,88,51,27,28,-68,66,-41,41,36,84,44,-16,91,49,71,-19,-94,28,-32,44,75,-57,66,51,-80,10,-35,-19,97,-65,70,63,86,-2,-9,94,-59,26,35,76,11,-21,-63,-21,-94,84,59,87,13,-96,31,-35,-53,-26,-84,-34,60,-20,23,58,15,-7,21,-22,67,88,-28,-91,14,-93,61,-98,-38,75,-19,-56,59,-83,-91,-51,-79,16,14,-56,90,6,-14,27,63,-91,-15,-22,-22,82,32,-54,47,-96,-69,-61,86,91,-60,-75,43,-3,-31,3,-9,-23,28,11,69,-81,31,59,25,-83,-36,-12,-75,48,42,-21,8,-26,24,-68,-23,31,-30,-60,0,-13,-36,-57,60,32,22,-49,85,-49,38,55,-54,-31,-9,70,-38,54,-65,-37,-20,76,42,64,-73,-57,95,-20,74,-57,19,-49,29,83,-7,-11,-8,-84,40,-45,-57,-45,86,-12,24,-46,-64,62,-91,-30,-74,-35,-76,44,-94,-73,86,77,7,37,-80,-74,87,48,85,-19,-85,-45,-27,31,9,-8,85,-28,79,-14,25,91,-51,10,-61,-49,74,-38,94,56,-12,57,34,71,-5,53,74,-18,-21,59,39,-30,90,-88,-99,-24,3,62,47,-40,-51,-27,-49,-26,82,-11,1,34,27,-5,-10,92,-48,-99,63,23,31,14,-94,-90,-49,44,-44,-59,33,-44,17,-64,-82,-36,-28,-57,13,0,-7,-4,88,70,-93,-7,-35,-4,-15,-6,-26,-75,93,-95,39,98,90,66,20,-54,-93,-47,-22,0,-35,-28,41,14,-8,-46,-86,84,26,-98,55,32,-29,96,-94,32,-33,-21,57,-39,-17,-27,-64,-50,-61,55,-28,-78,84,49,22,-73,-79,-37,40,12,-7,53,-26,-80,31,-94,51,-97,-98,56,34,-54,-88,-32,-17,-29,17,18,20,32,-49,91,54,-65,40,-47,-39,38,-8,-99,-73,84,30,0,-96,-38,5,32,-36,-16,-35,74,29,-23,-80,-88,47,36,29,-32,-54,79,-64,76,91,53,-71,-71,-9,-3,-93,17,-19,36,94,-38,97,-1,70,-62,82,-65,-87,11,11,-68,-1,-41,44,-71,3,89]))
# empty array
# push all sums into it, then return the highest number in it

# def maxSubArray(nums):
#     def add (x,y):
#         return x + y
#     for i in range(len(nums)):
#         # check sum of the whole thing
#         from_start = nums[i:]
#         sum_from_start = reduce(add,from_start)
#         print(sum_from_start)

#         # check sum of increasing start to same end
#         # check sum of any kind of middle subarray

# maxSubArray([-2,1,-3,4,-1,2,1,-5,4])

def canPlaceFlowers(flowerbed,n):
    i = 0
    counter = 0

    while i < len(flowerbed):
        if flowerbed[i] == 0:
            # Check if the current position and adjacent positions are empty
            if i == len(flowerbed) - 1 or (i < len(flowerbed) - 1 and flowerbed[i+1] == 0):
                flowerbed[i] = 1  # Plant a flower
                counter += 1
                i += 2  # Skip the next position as flowers cannot be planted adjacent
            else:
                i += 1  # Move to the next position
        else:
            i += 2  # Skip the current position as it's occupied

        if counter >= n:
            return True

    return counter >= n

# print(canPlaceFlowers([1,0,0,0,1], 1))

# You are given a string consisting of letters. The task 
# is to shuffle the letters and add numbers to each letter in the 
# format "letter number". The numbers start from 1 and increase by 1 for each letter.

# Example:

# Input: "aaiougnlrst"
# Output: "a1a2i3o4u5g6n7l8r9s10t11"

def numbered (s):
    count = 1
    # set up empty string
    numbered_string = []
    for i in s:
        # loop thru input, take the current element, append that into empty array
        numbered_string.append(i)
        # turn count into a string
        count_as_string = str(count)
        # take the idx+1 of the item from input and append that into the empty array
        numbered_string.append(count_as_string)
        # increase the count
        count += 1
    # turn numbered_string from an arry into a string
    result_string = "".join(numbered_string)
    # after the loop, return the created string
    return result_string

# output = "a1a2i3o4u5g6n7l8r9s10t11"
# print(output)
# print(numbered("aaiougnlrst"))

def sum_branches(arr):
    right_branch = []
    left_branch = []
    for num, idx in enumerate(arr):
#     odd indexes get pushed into left branch
        if idx % 2 != 0:
            right_branch.append(num)
#     even indexes go to the right branch
        if idx % 2 == 0:
            left_branch.append(num)
#     remove negative numbers
    for num in right_branch:
        if num < 0:
            right_branch.remove(num)
    for num in left_branch:
        if num < 0:
            left_branch.remove(num)
#     sum each branch
    def add(x,y):
        return x + y
    sum_of_right = reduce(lambda x,y: x + y, right_branch, 0)
    sum_of_left = reduce(add, left_branch)
#     if arr.length=0 or if branch sums are equal, return 0
    if len(arr) == 0 or sum_of_right == sum_of_left:
        return 0
#    else, return the larger branch
    if sum_of_right > sum_of_left:
        return "Right"
    if sum_of_right < sum_of_left:
        return "Left"  
    
# print(sum_branches([3,6,2,9,-1,10]))
    
def fizzBuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print('Fizzbuzz')
        # return 'Fizzbuzz'
    elif n % 3 == 0:
        print('Fizz')
        # return 'Fizz'
    elif n % 5 == 0:
        print('Buzz')
        # return 'Buzz'
    else:
        print(n)
        # return n

# print(fizzBuzz(1))

# @profile
def findRestaurant(list1, list2):
    sums = len(list1) + len(list2)
    common_strings = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                if i + j == sums:
                    common_strings.append(list1[i]) #add to common_strings list
                elif i + j < sums:
                    common_strings.clear()
                    common_strings.append(list1[i]) #add to common_strings list
                    sums = i + j # and change the value of sums
    return common_strings


start_time = time.time()
result = findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"])
end_time = time.time()


# print(f"Runtime: {1000 * (end_time - start_time):.6f} millisecondss")
# print(result)


sample_json = [
    {
        "title": "Baby (Feat. Ludacris) - Justin Bieber",
        "description": "Baby (Feat. Ludacris) by Justin Bieber on Grooveshark",
        "link": "http://listen.grooveshark.com/s/Baby+Feat+Ludacris+/2Bqvdq",
        "pubDate": "Wed, 28 Apr 2010 02:37:53 -0400",
        "pubTime": 1272436673,
        "TinyLink": "http://tinysong.com/d3wI",
        "SongID": "24447862",
        "SongName": "Baby (Feat. Ludacris)",
        "ArtistID": "1118876",
        "ArtistName": "Justin Bieber",
        "AlbumID": "4104002",
        "AlbumName": "My World (Part II);\nhttp://tinysong.com/gQsw",
        "LongLink": "11578982",
        "GroovesharkLink": "11578982",
        "Link": "http://tinysong.com/d3wI"
    },
    {
        "title": "Feel Good Inc - Gorillaz",
        "description": "Feel Good Inc by Gorillaz on Grooveshark",
        "link": "http://listen.grooveshark.com/s/Feel+Good+Inc/1UksmI",
        "pubDate": "Wed, 28 Apr 2010 02:25:30 -0400",
        "pubTime": 1272435930
    }
]

def get_keys(sample_json):
    for i in range(len(sample_json)):
        diction = sample_json[i]
        for key in diction:
            value = diction[str(key)]
            return value

# print(get_keys(sample_json))
# print(f"key is: {key}")
# val = key[1]
# print(f"val is: {val}")
# # print(val)

def reverse_string(string):
    new_string = ''.join(reversed(string))
    return new_string

# print(reverse_string("hello"))  # Output should be "olleh"
# print(reverse_string("python"))  # Output should be "nohtyp"
# print(reverse_string(""))  # Output should be ""


def is_palindrome(string):
    new_string = ''.join(reversed(string))
    if new_string == string:
        return True
    return False

# print(is_palindrome("radar"))  # Output should be True
# print(is_palindrome("hello"))  # Output should be False
# print(is_palindrome("A man, a plan, a canal, Panama"))  # Output should be True

# def count_vowels(string):
#     counter = 0
#     vowels = ['a','e','i','o','u']
#     for letter in string:
#         for vowel in vowels:
#             if letter.lower() == vowel:
#                 counter += 1
#     return counter

def count_vowels(string):
    vowels = ['a','e','i','o','u']
    counter = 0
    for letter in string:
        if letter.lower() in vowels:
            counter += 1
    return counter

# print(count_vowels("hello"))  # Output should be 2
# print(count_vowels("Python"))  # Output should be 1
# print(count_vowels("OpenAI"))  # Output should be 4
# print(count_vowels(""))  # Output should be 0

def average(list):
    # get length
    length = len(list)
    # sum the list
    def add(x,y):
        return x + y
    sum = reduce(add, list)
    # divide the sum by the length
    return sum / length

def avg(list):
    return sum(list) / len(list)

# print(avg([1, 2, 3, 4, 5]))

def common_elements(list_one, list_two):
    # common = []
    # for list_one_element in list_one:
    #     for list_two_element in list_two:
    #         if list_one_element == list_two_element and list_one_element not in common:
    #             common.append(list_one_element)
    # return common

    # OR
    
    common = []
    for element in list1:
        if element in list2 and element not in common:
            common.append(element)
    return common


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
# print(common_elements(list1, list2))

def find_duplicates(nums) -> list[int]:
    
    # if len(nums) <= 0:
    #     return 'List is Empty'
    
    duplicates = []
    # for i, val_one in enumerate(nums):
    #     for j,val_two in enumerate(nums):
    #         if nums[i] == nums[j] and i != j and nums[i] not in duplicates:
    #             duplicates.append(nums[i])
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j] and nums[i] not in duplicates:
                duplicates.append(nums[i])
    
    return duplicates

# print(find_duplicates([1, 2, 3, 4, 4, 5, 5, 6]))
# print(find_duplicates([1, 2, 3, 4, 5]))
# print(find_duplicates([]))
# print(find_duplicates([1,2,2,1,5,5,5,8]))
# print(find_duplicates('HeLLo'))

# MY WRONG ATTEMPT
def capitalize_words(string):
    #  split string into a list at the spaces
    words = string.split()
    #  loop thru the list and capitalize the 0 index
    for word in words:
        word[0].upper()
    #  join the list into a string
    capitalized_words = ' '.join(words)
    return capitalize_words

# CHATGPT'S SOLUTION:
def capitalizeWords(s):
    # Split the input string into words
    words = s.split()
    
    # Capitalize the first letter of each word
    capitalized_words = [word.capitalize() for word in words]
    
    # Join the capitalized words back into a string
    return ' '.join(capitalized_words)

# print(capitalize_words("hello world"))
# print(capitalize_words("the quick brown fox"))
# print(capitalize_words("what's up, doc?"))

def zigzags(numbers):
    if len(numbers) == 0:
        return [0]
        
    zigs = []
    for i in range(len(numbers)-2):
        if numbers[i+2]:
            if numbers[i] > numbers[i+1] and numbers[i+1] < numbers[i+2]:
                zigs.append(1)
            elif numbers[i] < numbers[i+1] and numbers[i+1] > numbers[i+2]:
                zigs.append(1)
            else:
                zigs.append(0)
            
    return zigs



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
# print("Sorted array:", sorted_list)


# MERGE SORT AS A SINGLE FUNCTION: **************
'''
def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: If the array has 0 or 1 elements, it is already sorted

    # Divide the array into two halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge the sorted halves
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
print("Sorted array:", sorted_list)

'''

def array_transformation(arr):
    b = [0] * len(arr)
    # b = []
    for i in range(len(arr)):
        b[i] += (arr[i-1] if i-1 >= 0 else 0) + arr[i] + (arr[i+1] if i+1 < len(arr) else 0)
        # b.append((arr[i-1] if i-1 >= 0 else 0) + arr[i] + (arr[i+1] if i+1 < len(arr) else 0))
    return b

# print(array_transformation([4,0,1,-2,3]))

# def pattern_source(pattern, source):
#     vowels = ['a','e','i','o','u']
#     counter = 0
#     pattern_list = pattern.split()
#     for i in range(len(source)):
#         arr = []
#         while len(arr) <= len(pattern):
#             if source[i] in vowels:
#                 arr.append(0)
#             else:
#                 arr.append(1)
#         if arr == pattern_list:
#             counter += len(arr)
#     return counter


# pattern = '010'
# source = 'amazing'

def pattern_source(pattern, source):
    # init vowels array
    vowels = ['a', 'e', 'i', 'o', 'u']
    # init an empty string 'compare_pattern'
    compare_pattern = ''
    # loop thru source and see if the character is in vowel (+= 0 to compare_pattern if it is, else +=1)
    for i in range(len(source)):
    # ensure compare_pattern length is = pattern length at the end
        current_character = source[i]
        if source[i] in vowels:
            compare_pattern += '0'
        else:
            compare_pattern += '1'
    answer = compare_pattern.count(pattern)
    
    return answer


# print(pattern_source('010', 'amazing'))  # expected output: 2

# Sliding Window: Sum example
def max_subarray_sum(arr, k):
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

# Example usage:
arr = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
k = 3
# print("Maximum sum of subarray of size", k, ":", max_subarray_sum(arr, k))

def sliding_window_template(arr, k):
    left = 0
    right = k - 1  # Initialize the right end of the window
    
    # Handle edge cases
    if len(arr) == 0 or k > len(arr):
        return None  # or handle it according to your problem
    
    # Initialize any necessary variables
    
    while right < len(arr):
        # Update window state
        # For example, calculate the sum of elements within the current window
        
        # Process the current window
        # For example, check if the sum of the current window is greater than the previous maximum sum
        
        # Handle any additional logic
        
        # Move the window by incrementing left and right pointers
        left += 1
        right += 1
    
    # Return any relevant results


def maxSlidingWindow(nums, k: int):
    max_array = []
    left_pointer = 0
    right_pointer = k
    # loop thru List for i in range(len(nums)-1):
    while right_pointer <= len(nums):
        # slice that portion of the List
        window = nums[ left_pointer : right_pointer ]
        # sum that portion
        window_max = max(window)
        # push the sum into max_array
        max_array.append(window_max)
        # increase left/right pointer += 1
        left_pointer += 1
        right_pointer += 1
    # return max_array
    return max_array

# print(maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))   # Expected Output: [3,3,5,5,6,7]

# numbers = [[1,2,3,4],[4,5,6],[7,8,9]]
# print(range(len(numbers[0]) - 2))

'''
if nums has all numbers from 1-9, then
'''
def sliding_matrix(nums):
    # create result array to return
    # loop through the matrix (set up the window here)
        # set up temp array to hold all values from current window (each iteration of the outer outer loop)
        # create a nested loop to check each int within each row
            # add each element from the current window to a temp array that we will check to see if it includes the data we want or not
        # check if temp array is true/false and append that to result array
    # return result array
    pass

'''
LOOP THRU A sliding matrix window and check if each of the values in that window are even. Then return an array with true/false for each window. the input matrix will be 2xn and the window should be 2x2.
'''
def even_window(nums):
    result = []
    n = len(nums[0])
    # loop & create 2x2 window
    for i in range(2):
        current_window = []
        # loop thru rows
        for row in nums:
            # nested loop thru cols
            for col in range(i, i+2):
                # append each element to current_window
                current_window.append(row[col])
        # check if current_window is all even or not
        # append true to result if so, else append false
        result.append((sum(current_window)) % 2 == 0)
    return result

# PROBLEM 2 FROM ASANA ASSESSMENT
'''
You are given numbers, a 3 * n matrix which contains only digits from 1 to 9. 
Consider a sliding window of size 3 x 3, which is sliding from left to right 
through the matrix numbers. The sliding window has n - 2 positions when sliding 
through the initial matrix.
Your task is to find whether or not each sliding window position contains all the 
numbers from 1 to 9 (inclusive). Return an array of length n - 2, where the ith 
element is true if the ith state of the sliding window contains all the numbers 
from 1 to 9, and false otherwise.
'''

def contains_all_numbers(numbers):
    # empty array to store result
    result = []
    n = len(numbers[0])
    counter = 0
    # for i in range(n - 2): #range(n-2) determines how long len(result) is and makes sure that the 'j' loop index range can fit inside the array (i.e: ensure that i+3 is a valid idx)
    while counter <= n-3:
        window = []
        for row in numbers:
            # for j in range(i, i + 3):
            for col in range(counter, counter + 3):
                window.append(row[col])
        result.append(len(set(window)) == 9)
        counter += 1
    return result

# This is what was submitted
def contains_all_numbers_GPT(numbers):
    result = []
    for i in range(len(numbers[0]) - 2):
        window = []
        for row in numbers:
            for col in range(i, i + 3):
                window.append(row[col])
        result.append(len(set(window)) == 9)
    return result



'''
You are given a list of lists grid representing a grid of integers. 
Each list in grid represents a row in the grid. Your task is to find 
the sum of each 2x2 subgrid within the grid and return a list of these sums.

For example, given the grid:
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

The 2x2 subgrids and their sums are:

Subgrid starting at (0, 0): [[1, 2], [4, 5]], sum = 1 + 2 + 4 + 5 = 12
Subgrid starting at (0, 1): [[2, 3], [5, 6]], sum = 2 + 3 + 5 + 6 = 16
Subgrid starting at (1, 0): [[4, 5], [7, 8]], sum = 4 + 5 + 7 + 8 = 24
Subgrid starting at (1, 1): [[5, 6], [8, 9]], sum = 5 + 6 + 8 + 9 = 28

So, the expected output would be [12, 16, 24, 28].

Your task is to implement a function sum_of_subgrids(grid) that takes the grid 
as input and returns a list containing the sums of all 2x2 subgrids.
'''

def sum_of_subgrids(grid):
    sums = []
    m = len(grid) #num of rows
    n = len(grid[0]) #num of columns
    for row in range(m - 1): #loop thru the num of rows
        for col in range(n - 1): #loop thru the cols within the rows
            window = [
                grid[row][col],
                grid[row][col +1],
                grid[row + 1][col],
                grid[row + 1][col + 1]
            ]
            sums.append(sum(window))
    return sums

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# print(sum_of_subgrids(grid))

def max_hourglass_sum(grid):
    sums = []
    m = len(grid) #num of rows
    n = len(grid[0]) #num of columns
    for row in range(m - 2): #loop thru the num of rows
        for col in range(n - 2): #loop thru the cols within the rows
            window = [
                grid[row][col],
                grid[row][col +1],
                grid[row][col +2],
                grid[row + 1][col + 1],
                grid[row + 2][col],
                grid[row + 2][col +1],
                grid[row + 2][col +2],
            ]
            sums.append(sum(window))
    return max(sums)

grid = [    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]

# print(max_hourglass_sum(grid))

def min_candies(nums):
    n = len(nums)
    candy = [1] * n
    for i in range(n):
        if nums[i+1] > nums[i]:
            candy[i+1] += 1
        elif nums[i+1] < nums[i]:
            candy[i] += 1
    return sum(candy)

nums = [1, 0, 2]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        l1_list = [l1.val]
        l2_list = [l2.val]
        current_l1_node = l1
        current_l2_node = l2
        # loop thru LL and append each node into its temp list
        if current_l1_node.next:
            next_node = current_l1_node.next
            l1_list.append(next_node.val)
            current_l1_node = current_l1_node.next
        if current_l2_node.next:
            next_node = current_l2_node.next
            l2_list.append(next_node.val)
            current_l2_node = current_l2_node.next
        # reverse and join the temp lists
        int_l1 = int(''.join(map(str, reversed(l1_list))))
        int_l2 = int(''.join(map(str, reversed(l2_list))))
        # get the sum
        the_sum = int_l1 + int_l2
        # add each number as a node in a new Linked List but in reverse order
        new_linked_list_head = None
        # Iterate through each digit of the sum in reverse order
        for digit in reversed(str(the_sum)):
            # Convert the digit to an integer and create a new node
            new_node = ListNode(int(digit))
            # Link the new node to the existing linked list
            new_node.next = new_linked_list_head
            # Update the head of the linked list to the new node
            new_linked_list_head = new_node
        return new_linked_list_head

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    # convert LLs to a list
    list_one = []
    list_two = []
    
    current_l1 = l1
    while current_l1:
        list_one.append(current_l1.val) #adds the next node to the list
        current_l1 = current_l1.next #changes current to the next node
        
    current_l2 = l2
    while current_l2:
        list_two.append(current_l2.val) #adds the next node to the list
        current_l2 = current_l2.next #changes current to the next node

    # reverse those lists and turn it into an integer
    int_l1 = int(''.join(map(str, reversed(list_one))))
    int_l2 = int(''.join(map(str, reversed(list_two))))
    
    # add the integer's together to get the sum
    reversed_sum = int_l1 + int_l2
    
    # Loop thru the sum and add each digit to a new linked list
    dummy = ListNode(0)
    current_node = dummy
    for i in range(reversed_sum):
        # if idx=0 then make this digit the head node
        if i == 0:
            dummy = ListNode(reversed_sum[i])
        # else set this digit as the next node
        else:
            current_node.next = ListNode(reversed_sum[i])
            current_node = current_node.next
    return dummy

def add_diagonals(matrix):
    n = len(matrix)
    sums = []
    # primary diagonal
    for i in range(n):
        diagonal = []
        #append to diagonal
        diagonal.append(matrix[i][i])
        # sum diagonal and append to sums list
        sums.append(sum(diagonal))
    # secondary diagonal
    for i in range(n):
        diagonal = []
        #append to diagonal
        diagonal.append(matrix[i][-i])
        # sum diagonal and append to sums list
        sums.append(sum(diagonal))
    return sum(sums)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# print(add_diagonals(matrix))

'''
Problem:
You are given a square matrix matrix of size n x n, where 
each cell contains an integer. Your task is to find the sum
of the elements in each row and return the list of sums.
'''
def row_sums(matrix):
    n = len(matrix)
    sums = []
    for row in matrix:
        sums.append(sum(row))
    return sums

# print(row_sums(matrix))

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def rotate_clockwise(matrix):
    n = len(matrix)
    rotated = [[0] * n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            rotated[col][n-1-row] = matrix[row][col]
    return rotated

# print(rotate_clockwise(matrix))

def rotate_counterClockwise(matrix):
    n = len(matrix)
    rotated = [[0] * n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            rotated[n-1-row][col] = matrix[col][row]
    return rotated

# print(rotate_counterClockwise(matrix))

def flip_matrix(matrix):
    n = len(matrix)
    flipped = [[0] * n for _ in range(n)]
    for row in range(n):
        flipped[row] = matrix[n-1-row]
    return flipped
# print(flip_matrix(matrix))

def flip_main_diagonal(matrix):
    n = len(matrix)
    flipped = [[0] * n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            flipped[row][col] = matrix[col][row]
    return flipped

# print(flip_main_diagonal(matrix))

def flip_secondary_diagonal(matrix):
    n = len(matrix)
    flipped = [[0] * n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            flipped[row][col] = matrix[n-1-col][n-1-row]
    return flipped

# print(flip_secondary_diagonal(matrix))

def bubbly(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

matrix = [
    [3, 3, 1, 1],
    [2, 2, 1, 2],
    [1, 1, 1, 2]
]

[
    [1, 1, 1, 1],
    [1, 2, 2, 2],
    [1, 2, 3, 3]
]
def diagonal_sort(matrix):
    n = len(matrix)
    m = len(matrix[0])
    sorted_matrix = [[0] * m for _ in range(n)]
    for i in range(n):
        for row in range(n-1):
            for col in range(m-1):
                current = matrix[row][col]
                compare_with = matrix[row + 1][col + 1]
                if matrix[row][col] > matrix[row + 1][col + 1]:
                    sorted_matrix[row][col] = matrix[row + 1][col + 1]
                    sorted_matrix[row + 1][col + 1] = matrix[row][col]
                else:
                    sorted_matrix[row][col] = matrix[row][col]
                    sorted_matrix[row + 1][col + 1] = matrix[row + 1][col + 1]
    return sorted_matrix
print(diagonal_sort(matrix))


matrix = [
    [3, 3, 1, 1],
    [2, 2, 1, 2],
    [1, 1, 1, 2]
]
def diagonal_sort(matrix):
    # Get dimensions of the matrix
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Iterate over each diagonal line
    for diagonal_idx in range(rows + cols - 1): #rows + cols - 1 calculates the number of diagonal lines in a grid
        diagonal_elements = []
        
        # Extract elements along the current diagonal
        for row in range(max(0, diagonal_idx - cols + 1), min(rows, diagonal_idx + 1)):
            col = diagonal_idx - row
            diagonal_elements.append(matrix[row][col])
        
        # Sort the extracted elements
        diagonal_elements.sort()
        
        # Place the sorted elements back into the matrix along the same diagonal
        for row in range(max(0, diagonal_idx - cols + 1), min(rows, diagonal_idx + 1)):
            col = diagonal_idx - row
            matrix[row][col] = diagonal_elements.pop(0)
    
    return matrix
