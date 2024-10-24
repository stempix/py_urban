from private.test_runner import test_runner

def get_matrix(n, m, value):
    # Для того чтобы не создавать лишние вложенные пустые списки
    if m <= 0:
        return []
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)

    return matrix

test_data = (
    [2, 2, 10], # Test 1
    [3, 5, 42], # Test 2
    [4, 2, 13], # Test 3
    [2, 3, -7], # Test 4
    [1, 1, 1],  # Test 5
    [0, 1, 10], # Test 6
    [1, 0, 10], # Test 7
    [0, 0, 0],  # Test 8
    [-1, 1, 2], # Test 9
    [1, -1, 2]  # Test 10
)

test_expect = (
    [[10, 10], [10, 10]],                                               # Test 1
    [[42, 42, 42, 42, 42], [42, 42, 42, 42, 42], [42, 42, 42, 42, 42]], # Test 2
    [[13, 13], [13, 13], [13, 13], [13, 13]],                           # Test 3
    [[-7, -7, -7], [-7, -7, -7]],                                       # Test 4
    [[1]],                                                              # Test 5
    [],                                                                 # Test 6
    [],                                                                 # Test 7
    [],                                                                 # Test 8
    [],                                                                 # Test 9
    []                                                                  # Test 10
)

test_runner(test_data, test_expect, get_matrix)