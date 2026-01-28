# function which creates spiral matrix
def spiral_matrix(n):
    matrix = [[0]*n for _ in range(n)]
    
    num = 1
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    
    while left <= right and top <= bottom:
        # From left to right
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
        
        # Top down
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        
        # From right to left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1
        
        # From bottom to top
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
    
    return matrix

# Input
n = int(input())

# Generating a spiral
result = spiral_matrix(n)

# Output
for row in result:
    print(' '.join(map(str, row)))
