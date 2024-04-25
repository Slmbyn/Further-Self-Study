matrix = [
    [3, 3, 1, 1],
    [2, 2, 1, 2],
    [1, 1, 1, 2]
]

# SUM ROWS
def sum_rows(matrix):
    sums = []
    for row in matrix:
        sums.append(sum(row))
    return sums
# print(sum_rows(matrix))

def sum_cols(matrix):
    sums = []
    for col in range(len(matrix[0])):
        curr_col = []
        for row in range(len(matrix)):
            curr_col.append(matrix[row][col])
        sums.append(sum(curr_col))
    return sums
# print(sum_cols(matrix))

# SUM DIAGONALS
def sum_diagonals(matrix):
    m = len(matrix)
    n = len(matrix[0])

    diagonals = [[] for _ in range(n+m-1)]
    
    for i in range(m):
        for j in range(n):
            diagonals[i-j].append(matrix[i][j])
            
    sums = []
    for row in diagonals:
        sums.append(sum(row))
    
    return sums
# print(sum_diagonals(matrix))

def sum_main_diagonal(matrix):
    m = len(matrix)
    n = len(matrix[0])
    
    if n != m:
        raise ValueError
    
    main_diag = []
    
    for i in range(n):
        main_diag.append(matrix[i][i])
    
    return sum(main_diag)
    
matrix = [
    [3, 3, 1],
    [2, 2, 1, 2],
    [1, 1, 1, 2]
]
# print(sum_main_diagonal(matrix))

# SLIDING WINDOW
'''
You are given numbers, a n * n matrix which contains only digits from 1 to 9. 
Consider a sliding window of size 3 x 3, which is sliding from left to right 
through the matrix numbers. The sliding window has n - 2 positions when sliding 
through the initial matrix.
Your task is to find whether or not each sliding window position contains all the 
numbers from 1 to 9 (inclusive). Return an array of length n - 2, where the ith 
element is true if the ith state of the sliding window contains all the numbers 
from 1 to 9, and false otherwise.
'''

numbers = [
    [1, 2, 3, 2, 5],
    [4, 5, 6, 8, 6],
    [7, 8, 9, 4, 7],
    [1, 2, 3, 2, 5],
    [4, 5, 6, 8, 6]
]

def contains_all_numbers(numbers):
    m = len(numbers)
    n = len(numbers[0])

    result = []
    
    for i in range(n-2):
        
        curr_window = []
        for row in range(3):
            for col in range(i, i + 3):
                # append to curr_window
                curr_window.append(numbers[row][col])
        # if curr_window includes all nums, append True to result
        if sorted(curr_window) == list(range(1,10)):
            result.append(True)
        else:
            result.append(False)
            
    return result
            
    
# print(contains_all_numbers(numbers))

# ROTATE MATRIX
matrix = [
    [3, 3, 1, 1],
    [2, 2, 1, 2],
    [1, 1, 1, 2]
]

[[1, 2, 3], 
 [0, 0, 0], 
 [0, 0, 0], 
 [0, 0, 0]]

def rotate_90(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    rotated = [[0] * n for _ in range(m)]
    
    for row in range(m):
        for col in range(n):
            rotated[row][len(rotated[0]) - 1 - col] = matrix[col][row]
    
    return rotated
    
# print(rotate_90(matrix))
# FLIP MATRIX
matrix = [
    [3, 3, 7],
    [2, 2, 1],
    [1, 5, 8]
]
def flip_diagonal(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    flipped = [[0] * m for _ in range(n)]
    
    for row in range(n):
        for col in range(m):
            flipped[col][row] = matrix[row][col]
            
    return flipped

print(flip_diagonal(matrix))
[[3, 2, 1],
 [3, 2, 5], 
 [7, 1, 8]]


# SORT DIAGONALLY

def sort_diagonal(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    diagonals = [[] for _ in range(m+n-1)]
    
    for row in range(n):
        for col in range(m):
            diagonals[row-col].append(matrix[row][col])
            
    # sort it
    for row in diagonals:
        row.sort(reverse=True)
    
    for row in range(n):
        for col in range(m):
            matrix[row][col] = diagonals[row-col].pop()
        
    return matrix

# print(sort_diagonal(matrix))
    
# [[1, 1, 1, 1], 
#  [1, 2, 2, 2], 
#  [1, 2, 3, 3]]