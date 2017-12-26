import numpy as np
import scipy.linalg as lg

t = 100
x = np.array([1, 0, 0, 0, 0, 0])
V = np.array([[0, 1, 0, 0], [0, 0, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]])
print(V)
D = np.diag(np.sum(V, axis=1))
print(D)
M = V.transpose() - D
print(M)
for t in range(0, 10):
    dot = lg.expm(M * t).dot(x)
    print(dot)
    print(dot.sum())


# print(lg.expm(np.array([[0, -1], [1, 0]]) * t))
# print(np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]]))
