import random
import math
import matplotlib.pyplot as plt


def simulation(initial_money, desired_money, money_perc):
    print("start gamble :")
    ite = 0
    money_perc = max(min(1.0, money_perc), 0)
    while 0 < initial_money < desired_money:
        initial_money = math.floor(initial_money)
        r = random.randint(0, 1)
        guess = random.randint(0, 1)
        if r == guess:
            initial_money += money_perc * initial_money
        else:
            initial_money -= money_perc * initial_money
        ite += 1
        print(initial_money)
    return [initial_money, ite]


def simulation_stats(n):
    ite = 0
    money = 0
    for i in range(0, n):
        v = simulation(10, 100, 0.8)
        money += v[0]
        ite += v[1]
    print("Statistics")
    print("Average money: " + str(1.0 * money / n))
    print("Average ite: " + str(1.0 * ite / n))


def expected_value(n, samples, initial_money, money_perc):
    acc = 0
    for j in range(0, samples):
        money = initial_money
        for i in range(0, n):
            r = random.randint(0, 1)
            guess = random.randint(0, 1)
            if r == guess:
                money += money_perc * money
            else:
                money -= money_perc * money
        acc += money
    return 1.0 * acc / samples


def psi_closed(n, k):
    ide = 1
    acm = 1
    for i in range(0, k):
        ide = (ide * n) / acm
        acm += 1
        n -= 1
    return ide


def pow_int(x, i):
    if i == 0:
        return 1
    elif i == 1:
        return x
    else:
        q = math.floor(i / 2)
        r = i % 2
        if r == 0:
            return pow_int(x * x, q)
        else:
            return x * pow_int(x * x, q)


def expected_value_analytic(n, initial_money, money_perc):
    p = 0.5
    exp_log_x = math.log(initial_money) + n * (math.log(1 + money_perc) * p + math.log(1 - money_perc) * (1 - p))
    return math.exp(exp_log_x)


# Main
maxSamples = 1000
n = 1000
initial_money = 1000
r = 0.2
print("Expected Value of " + str(n) + " gambles")
print("Simulation\t Analytic")
accNumeric = []
accAnalytic = []
for i in range(1, maxSamples, 100):
    accNumeric.append(expected_value(n, i, initial_money, r))
    accAnalytic.append(expected_value_analytic(n, initial_money, r))
    print(str(i) + "\t" + str(expected_value(n, i, initial_money, r)) + "\t" + str(
        expected_value_analytic(n, initial_money, r)))

plt.plot(accNumeric, 'g', label='numeric')
plt.plot(accAnalytic, 'r', label='analytic')
plt.legend()
plt.show()
