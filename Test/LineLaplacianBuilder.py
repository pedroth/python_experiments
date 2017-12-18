import math

import numpy as np

from MatrixExp import matrix_exp_eigen


def get_line_laplacian_matrix(n):
    assert n > 1
    matrix = np.zeros([n, n])
    # interior
    for i in range(1, n - 1):
        matrix[i, i - 1] = -1
        matrix[i, i + 1] = -1
        matrix[i, i] = 2
    # boundary
    matrix[0, 0] = 1
    matrix[0, 1] = -1
    matrix[n - 1, n - 2] = -1
    matrix[n - 1, n - 1] = 1
    return matrix


def get_line_laplacian_eigen(n):
    assert n > 1
    eigen_vectors = np.zeros([n, n])
    eigen_values = np.zeros([n])

    for j in range(1, n + 1):
        theta = math.pi * (j - 1) / (2 * n)
        sin = math.sin(theta)
        eigen_values[j - 1] = 4 * sin * sin
        if j == 0:
            sqrt = 1 / math.sqrt(n)
            for i in range(1, n + 1):
                eigen_vectors[i - 1, j - 1] = sqrt
        else:
            for i in range(1, n + 1):
                theta = (math.pi * (i - 0.5) * (j - 1)) / n
                math_sqrt = math.sqrt(2.0 / n)
                eigen_vectors[i - 1, j - 1] = math_sqrt * math.cos(theta)
    return eigen_vectors, eigen_values


if __name__ == "__main__":
    dim = 10
    print(get_line_laplacian_matrix(dim))
    U, s = get_line_laplacian_eigen(dim)
    signal = np.random.rand(10)
    matrix_exp_eigen()
