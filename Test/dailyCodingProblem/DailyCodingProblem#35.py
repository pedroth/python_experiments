def swap(x, i, j):
    assert i >= 0 and i < len(x) and j >= 0 and j < len(x)
    t = x[i]
    x[i] = x[j]
    x[j] = t


def order_symbols(x, symbols):
    assert bool(symbols)
    initial_index = []
    symbols_histogram = []
    symbol2index = {}
    already_fixed = []

    for i in range(len(symbols)):
        symbol2index[symbols[i]] = i
        initial_index.append(0)
        symbols_histogram.append(0)

    for i in x:
        symbols_histogram[symbol2index[i]] += 1
        already_fixed.append(False)

    for i in range(1, len(symbols)):
        initial_index[i] = symbols_histogram[i - 1] + initial_index[i - 1]

    for i in range(len(x)):
        if not already_fixed[i]:
            while True:
                s = x[i]
                j = initial_index[symbol2index[s]]
                already_fixed[j] = True
                swap(x, i, j)
                initial_index[symbol2index[s]] += 1
                if i == j:
                    break
    return x


if __name__ == '__main__':
    l1 = ['G', 'B', 'R', 'R', 'B', 'R', 'G']  # list(3 * 'RGB')
    print(l1)
    print(order_symbols(l1, ['R', 'G', 'B']))
