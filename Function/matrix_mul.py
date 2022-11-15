def matrix_mul(a, b):

    res = [[0 for i in range(len(b[0]))] for j in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                res[i][j] += a[i][k] * b[k][j]

    return res


a = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
b = [[5, 8, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1]]
print(matrix_mul(a, b))
