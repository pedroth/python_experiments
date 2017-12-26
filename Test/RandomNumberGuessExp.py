import random
import math
import matplotlib.pyplot as plt


def randomSearch1(x, xmin, xmax):
    guess = xmin
    while guess != x:
        guess += 1
    return guess


def randomSearch2(x, xmin, xmax):
    ite = 0
    guess = (xmin + xmax) / 2
    while guess != x:
        if guess < x:
            ite += 1
            xmin = guess
            guess = math.ceil((xmin + xmax) / 2)
        elif guess > x:
            ite += 1
            xmax = guess
            guess = math.floor((xmin + xmax) / 2)
        else:
            break
    return ite


def randomSearch3(x, xmin, xmax):
    guess = random.randint(xmin, xmax)
    ite = 0
    while guess != x:
        ite += 1
        guess = random.randint(xmin, xmax)
    return ite


def mySum(x):
    acc = 0
    for i in range(0, len(x)):
        acc += x[i]
    return acc


def dot(x, y):
    acc = 0
    for i in range(0, len(x)):
        acc += x[i] * y[i]
    return acc


def linearReg(x, y):
    n = len(x)
    xx = dot(x, x)
    yx = dot(y, x)
    x1 = mySum(x)
    y1 = mySum(y)
    b = 1.0 * (xx * y1 - x1 * (yx + x1)) / (n * xx)
    m = 1.0 * (yx - b * x1) / xx
    return [m, b]


def linearModel(x, m, b):
    return m * x + b


n = 1000

x = []
y1 = []
y2 = []
y3 = []

for i in range(1, n + 1):
    r = random.randint(1, i)
    x.append(i)
    y1.append(randomSearch1(r, 1, i))
    y2.append(randomSearch2(r, 1, i))
    y3.append(randomSearch3(r, 1, i))

model = [linearReg(x, y1), linearReg(x, y2), linearReg(x, y3)]

print('Range' + '\t' + 'BF Ite' + '\t' + "DQ Ite" + '\t' + 'Random Num')
for i in range(1, n + 1):
    print(str(i) + "\t" + str(y1[i - 1]) + "\t" + str(y2[i - 1]) + "\t" + str(y3[i - 1]) + "\t" + str(
        linearModel(i, model[0][0], model[0][1])) + "\t" + str(linearModel(i, model[1][0], model[1][1])) + "\t" + str(
        linearModel(i, model[2][0], model[2][1])))

print("\n" * 3)

plt.plot(x, y3, 'b', x, [linearModel(i, model[2][0], model[2][1]) for i in range(1, n + 1)], 'b-')
plt.plot(x, y1, 'r', x, [linearModel(i, model[0][0], model[0][1]) for i in range(1, n + 1)], 'r-')
plt.plot(x, y2, 'g', x, [linearModel(i, model[1][0], model[1][1]) for i in range(1, n + 1)], 'g-')
plt.xlabel('guess')
plt.ylabel('number of iterations')
plt.show()
