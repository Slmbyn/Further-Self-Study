# SUM MATRICIES
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

# rotate matrix clockwise (90degrees)
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

# Rotate counterclockwise
def rotate_counter(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    rotated = [[0] * n for _ in range(n)]
    
    for row in range(n):
        for col in range(m):
            rotated[m-1-col][row] = matrix[row][col]
    
    print(rotated)
    return

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotate_counter(matrix)
    
    
# Flip matrix
# Flip on main diagonal
# Flip on secondary diagonal
# Sliding window
# Sort diagonally

