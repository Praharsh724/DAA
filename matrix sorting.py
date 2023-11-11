def rotate_matrix_anticlockwise(matrix):
    transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    rotated_matrix = transposed_matrix[::-1]

    return rotated_matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original Matrix:")
print_matrix(matrix)

rotated_matrix = rotate_matrix_anticlockwise(matrix)

print("\nMatrix Rotated by 90 Degrees anticlockwise:")
print_matrix(rotated_matrix)