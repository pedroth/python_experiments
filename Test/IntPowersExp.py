import time
import matplotlib.pyplot as plt


def int_pow_iterative(x, n):
    assert isinstance(n, int)
    acc = 1
    for i in range(0, n):
        acc *= x
    return acc


def int_pow_recursive(x, n):
    assert isinstance(n, int)
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        if n % 2 == 0:
            return int_pow_recursive(x * x, int(n / 2))
        else:
            return x * int_pow_recursive(x * x, int(n / 2))


def int_pow_squaring(x, n):
    assert isinstance(n, int)
    k = int(n / 2)
    r = n % 2
    acc = 1
    for i in range(0, k):
        acc *= x * x
    if r == 1:
        acc *= x
    return acc


def measure_pow_time(pow, N):
    x = 2
    acc = []
    assert N >= 0
    n = 0
    for i in range(0, N):
        start = time.time()
        pow(x, n)
        acc.append(time.time() - start)
        n += 10
    return acc


N = 5000
time_iterative = measure_pow_time(int_pow_iterative, N)
time_recursive = measure_pow_time(int_pow_recursive, N)
time_squaring = measure_pow_time(int_pow_squaring, N)
plt.figure(num=None, figsize=(10, 8), dpi=80, facecolor='w', edgecolor='k')
plt.plot(time_iterative, 'r', time_recursive, 'b', time_squaring, 'g')
plt.show()
