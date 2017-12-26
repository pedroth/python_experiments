import math
import matplotlib.pyplot as plt

def quadratic_simulation(a, beta, v, alpha):
    x = beta + v
    ite = 0
    while math.fabs(x - beta) > 1E-3:
        x = x * (1.0 - 2.0 * a * alpha) + 2 * a * beta * alpha
        ite += 1
    return ite


samples = 1000
a = 4.0
beta = 0.0
d = 100.0
epsilon = 1E-3
alpha = []
n = []
simulation = []
for i in range(0, samples):
    alpha.append((1.0 * (i + 1)) / (samples - 1))
    batata = epsilon / (4 * a * a * d)
    cebola = 1 - 2 * a * alpha[i]
    # print(str(alpha[i]) + "\t" + str(batata) + "\t" + str(cebola))
    if batata <= 0 or cebola <= 0 or math.log(cebola) == 0.0:
        continue
    n.append(math.log(batata) / math.log(cebola))
    simulation.append(quadratic_simulation(a, beta, d, alpha[i]))
    print(str(alpha[i]) + "\t" + str(simulation[i]) + "\t" + str(n[i]))

plt.plot(alpha[:len(n)], simulation,'b', alpha[:len(n)], n, 'g')
plt.xlabel('alpha')
plt.ylabel('number of iterations')
plt.show()