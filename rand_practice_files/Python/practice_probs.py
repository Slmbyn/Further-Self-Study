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

print(capitalize_words("hello world"))
print(capitalize_words("the quick brown fox"))
print(capitalize_words("what's up, doc?"))