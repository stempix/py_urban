def get_matrix(n, m, value):
    # Для того, чтобы не создавать лишние вложенные пустые списки
    if m <= 0:
        return []
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)

    return matrix

# Test cases:
result_1    = get_matrix(2, 2, 10)
result_2    = get_matrix(3, 5, 42)
result_3    = get_matrix(4, 2, 13)
result_4    = get_matrix(2, 3, -7)
result_5    = get_matrix(1, 1, 1)
result_6    = get_matrix(0, 1, 10)
result_7    = get_matrix(1, 0, 10)
result_8    = get_matrix(0, 0, 0)
result_9    = get_matrix(-1, 1, 2)
result_10   = get_matrix(1, -1, 2)

# Test results output:
print("Test 1:\t", result_1)    # Expected: [[10, 10], [10, 10]]
print("Test 2:\t", result_2)    # Expected: [[42, 42, 42, 42, 42], [42, 42, 42, 42, 42], [42, 42, 42, 42, 42]]
print("Test 3:\t", result_3)    # Expected: [[13, 13], [13, 13], [13, 13], [13, 13]]
print("Test 4:\t", result_4)    # Expected: [[-7, -7, -7], [-7, -7, -7]]
print("Test 5:\t", result_5)    # Expected: [[1]]
print("Test 6:\t", result_6)    # Expected: []
print("Test 7:\t", result_7)    # Expected: []
print("Test 8:\t", result_8)    # Expected: []
print("Test 9:\t", result_9)    # Expected: []
print("Test 10:", result_10)    # Expected: []