import math
import matplotlib.pyplot as plt


def powInt(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        q = math.floor(n / 2)
        r = n % 2
        if r == 0:
            return powInt(x * x, q)
        else:
            return x * powInt(x * x, q)


def expEuler(x, n):
    if n == 0:
        return 1
    else:
        return powInt(1.0 + (1.0 * x / n), n)


def expTaylor(x, n):
    acc = 0
    for k in range(0, n + 1):
        acc += (1.0 * powInt(x, k)) / math.factorial(k)
    return acc


def expHybrid(x, n, k):
    if n == 0:
        return 1
    else:
        acc = 0
        t = (1.0 * x) / n
        for l in range(0, k + 1):
            acc += (1.0 * powInt(t, l)) / math.factorial(l)
        return powInt(acc, n)


def exp_experiment(t, n):
    for i in range(0, n):
        print(str(i) + "\t" + str(expEuler(t, i)) + "\t" + str(expHybrid(t, i, 2)) + "\t" + str(
            expHybrid(t, i, 3)) + "\t" + str(
            expHybrid(t, i, 10)) + "\t" + str(expTaylor(t, i)) + "\t" + str(
            math.exp(t)))


def exp_error_experiment(t, n):
    exp = math.exp(t)
    acc = [[], [], [], [], []]
    for i in range(0, n):
        acc[0].append(math.fabs(expEuler(t, i) - exp))
        acc[1].append(math.fabs(expTaylor(t, i) - exp))
        acc[2].append(math.fabs(expHybrid(t, i, 2) - exp))
        acc[3].append(math.fabs(expHybrid(t, i, 3) - exp))
        acc[4].append(math.fabs(expHybrid(t, i, 10) - exp))
        print(str(i) + "\t" + str(acc[0][i]) + "\t" + str(acc[1][i]) + "\t" + str(acc[2][i]) + "\t" + str(
            acc[3][i]) + "\t" + str(acc[4][i]))
    plt.plot(acc[0], 'r', label='euler')
    plt.plot(acc[1], 'g', label='taylor')
    plt.plot(acc[2], 'b', label='hybrid2')
    plt.plot(acc[3], 'c', label='hybrid3')
    plt.plot(acc[4], 'y', label='hybrid10')
    plt.xlabel('iterations')
    plt.ylabel('error')
    plt.legend()
    plt.show()


# exp_experiment(100, 150)
exp_error_experiment(10, 150)
