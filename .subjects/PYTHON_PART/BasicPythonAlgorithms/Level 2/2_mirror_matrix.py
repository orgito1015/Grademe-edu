def mirror_matrix(matrix: list[list[int]]) -> list:
    result = []
    for row in matrix:
        result.append(row[::-1])
    return result

# testing
print(mirror_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))