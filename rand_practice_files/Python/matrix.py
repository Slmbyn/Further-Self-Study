# SUM MATRICIES ----------------------------------------------------------------------
def add_matricies(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions for addition")
    
    n = len(matrix1)
    m = len(matrix1[0])
    
    result = [[0] * n for _ in range(n)]
    
    for row in range(n):
        for col in range(m):
            sum = matrix1[row][col] + matrix2[row][col]
            result[row][col] = sum
    
    return result

# rotate matrix clockwise (90degrees) ----------------------------------------------------------------------
def rotate_90(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    rotated = [[0] * n for _ in range(n)]
    
    for row in range(n):
        for col in range(m):
            # [m-1-row] will stay the same until inner loop is done. Meaning, we will only be changing the values in that column, until 'row' changes
            #  since [m-1-row] stays the same and 'col' changes, we will be working our way down the same column until its done. Then row changes, which changes [m-1-row], which changes which column we work with
            rotated[col][m-1-row] = matrix[row][col]
    
    print(rotated)
    return

# Rotate counterclockwise ----------------------------------------------------------------------
def rotate_counter(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    rotated = [[0] * n for _ in range(n)]
    
    for row in range(n):
        for col in range(m):
            rotated[m-1-col][row] = matrix[row][col]
    
    print(rotated)
    return
# rotate_counter(matrix)

# Flip matrix ----------------------------------------------------------------------
def flip_matrix(matrix):
    n = len(matrix)
    # init an empty matrix
    result = [[0] * n for _ in range(n)]
    # loop thru the rows
    for row in range(n):
        # assign the value of the first row in new matrix to be last row in input matrix
        result[row] = matrix[ n - row - 1 ]
    return result
# print(flip_matrix(matrix))

# Flip on main diagonal ----------------------------------------------------------------------
def flip_main_diagonal(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    if n != m:
        raise ValueError('Must be a square matrix')

    flipped = [[0] * n for _ in range(n)]
    
    for row in range(n):
        for col in range(n):
            flipped[row][col] = matrix[col][row]
    
    return flipped
# print(flip_main_diagonal(matrix))


# Flip on secondary diagonal ----------------------------------------------------------------------
def flip_second_diagonal(matrix):
    n = len(matrix)
    flipped = [[0] * n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            flipped[row][col] = matrix[n-1-col][n-1-row]
    return flipped
# print(flip_second_diagonal(matrix))

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Add Diagonals ----------------------------------------------------------------------
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


# Sort diagonally ----------------------------------------------------------------------
# TOP RIGHT -> BOTTOM LEFT
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

matrix = [
    [3, 3, 1, 1],
    [2, 2, 1, 2],
    [1, 1, 1, 2]
]

# Expected Output:
# [[1, 1, 1, 1],
#  [1, 2, 2, 2],
#  [1, 2, 3, 3]]

def sort_diagonal(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    sorted_matrix = [[0] * m for _ in range(n)]
    
    for row in range(n):
        col = 0
        while matrix[row+1][col+1]:
            # logic for sorting the diagonal
            col += 1
            pass
        
    for col in range(m):
        row = 0
        while matrix[row+1][col+1]:
            # logic for sorting the diagonal
            row += 1
            pass
        
    return sort_diagonal


def flip_mat(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    flipped_mat = [[0] * m for _ in range(n)]
    
    for row in range(n):
        flipped_mat[row] = matrix[n-row-1]
    
    return flipped_mat

# print(flip_mat(matrix))

def flip_cols(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    result = [[0] * m for _ in range(n)]
    
    for row in range(n):
        for col in range(m):
            result[row][col] = matrix[row][m-1-col]
    
    return result
# print(flip_cols(matrix))

def flip_main_diag(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    result = [[0] * m for _ in range(n)]
    
    

diagonals = [[0] for _ in range(3 + 4 - 1)]
# print(diagonals)

def sort_diagonal(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    diagonals = [[] for _ in range(n + m - 1)] # [[], [], [], [], [], []]
    
    # Populate diagonals
    for i in range(n):
        for j in range(m):
            diagonals[i - j].append(matrix[i][j])
    
    # Sort diagonals
    for diagonal in diagonals:
        diagonal.sort(reverse=True)
    
    # Place sorted values back into matrix
    for i in range(n):
        for j in range(m):
            matrix[i][j] = diagonals[i - j].pop()
    
    return matrix

matrix = [
    [3, 3, 1, 1],
    [2, 2, 1, 2],
    [1, 1, 1, 2]
]
'''
expected output:
[1, 1, 1, 1]
[1, 2, 2, 2]
[1, 2, 3, 3]

'''

sorted_matrix = sort_diagonal(matrix)
for row in sorted_matrix:
    print(row)


