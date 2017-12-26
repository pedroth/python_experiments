import random
import math
import matplotlib.pyplot as plt


# data : list of things
# j : a thing
# return number of things in data that are equal to j
def count(data, j):
    acc = 0
    for i in range(len(data)):
        if data[i] == j:
            acc += 1
    return acc


# n : is the number of the data points
# m : is the number of states
# return histogram of the data
def simple_simulation(n, m):
    data = []
    histogram = []
    p = []
    for i in range(n):
        r = random.randint(0, m - 1)
        data.append(r)
    for j in range(m):
        histogram.append(count(data, j))
    return histogram


# histogram : histogram of the data ( x-axis is the state number, y-axis is the frequency of each state)
def max_entropy_estimate(histogram, alpha):
    p = []
    acc = 0
    for i in range(len(histogram)):
        pval = math.exp(histogram[i] / alpha)
        p.append(pval)
        acc += pval
    for i in range(len(p)):
        p[i] *= 1 / acc
    return p


# histogram : histogram of the data ( x-axis is the state number, y-axis is the frequency of each state)
def max_likelihood_estimate(histogram):
    p = []
    acc = 0
    for i in range(len(histogram)):
        pval = histogram[i]
        p.append(pval)
        acc += pval
    for i in range(len(p)):
        p[i] *= 1.0 / acc
    return p


histogram = simple_simulation(100, 10)
alpha = [1, 2, 3, 4, 5, 10]
pE = [max_entropy_estimate(histogram, i) for i in alpha]
p = max_likelihood_estimate(histogram)
for i in range(len(pE)):
    c = 1.0 - (1.0 * i) / len(pE)
    plt.plot(pE[i], color=(c, c, c))
plt.plot(p, 'g')
plt.xlabel('#states')
plt.ylabel('probability')
plt.show()
