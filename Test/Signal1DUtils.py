import numpy as np


def find_local_max(signal):
    dim = signal.shape[0]
    ans = np.zeros(dim - 2)
    for i in range(2, dim):
        dxf = signal[i - 1] - signal[i]
        dxb = signal[i - 1] - signal[i - 2]
        ans[i - 2] = 1.0 if dxf > 0 and dxb > 0 else 0.0
    return ans > 0.5
