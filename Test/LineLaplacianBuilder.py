import numpy as np

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

    for j in range(0, n):
        theta = np.pi * j / (2 * n)
        sin = np.sin(theta)
        eigen_values[j] = 4 * sin * sin
        if j == 0:
            sqrt = 1 / np.sqrt(n)
            for i in range(0, n):
                eigen_vectors[i, j] = sqrt
        else:
            for i in range(0, n):
                theta = (np.pi * i * j) / n
                math_sqrt = np.sqrt(2.0 / n)
                eigen_vectors[i, j] = math_sqrt * np.cos(theta)
    return eigen_vectors, eigen_values

