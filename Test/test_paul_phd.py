import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# From Signal1DUtils
def find_local_max(signal):
    dim = signal.shape[0]
    ans = np.zeros(dim - 2)
    for i in range(2, dim):
        dxf = signal[i - 1] - signal[i]
        dxb = signal[i - 1] - signal[i - 2]
        ans[i - 2] = 1.0 if dxf > 0 and dxb > 0 else 0.0
    return ans > 0.5

# From MatrixExp
def matrix_exp_eigen(U, s, t, x):
    exp_diag = np.diag(np.exp(s * t), 0)
    return U.dot(exp_diag.dot(U.transpose().dot(x)))

# From LineLaplacianBuilder
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

def smooth(t, signal):
    dim = signal.shape[0]
    U, s = get_line_laplacian_eigen(dim)
    return matrix_exp_eigen(U, -s, t, signal)


if __name__ == "__main__":
    # read signal from csv, and take first 1011 data points
    xsignal = pd.read_csv('resources/test_data.txt', sep='\t', header=None).values[0:1010, 2]
    signal = pd.read_csv('resources/test_data.txt', sep='\t', header=None).values[0:1010, 3]

    # smoothing parameter
    t = 100
    # Signal smoothing
    smoothed_signal = smooth(t, signal)
    # find local maximum minimum indexes
    local_max_index = find_local_max(smoothed_signal)

    # plot smooth and normal signal
    plt.plot(xsignal, signal)
    plt.plot(xsignal, smoothed_signal, 'r-')

    # draw local maximum
    stem = np.zeros(xsignal.shape)
    stem[local_max_index] = 1
    plt.stem(xsignal, np.max(smoothed_signal) * stem)

    plt.show()
    pd.DataFrame({'centers': xsignal[local_max_index], 'max_values': signal[local_max_index]}).to_csv("output.csv", index=False)