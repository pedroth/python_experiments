import unittest


def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair


def car(pair):
    def g(a, b):
        return a

    return pair(g)


def cdr(pair):
    def g(a, b):
        return b

    return pair(g)


def assertEqual(x, y):
    return x == y


class TestPair(unittest.TestCase):
    def test_pair_basic(self):
        self.assertEqual(car(cons(1, 2)), 1)
        self.assertEqual(cdr(cons(3, 2)), 2)

    def test_pair_complex(self):
        self.assertEqual(car(car(cons(cons(1, 2), 3))), 1)


if __name__ == '__main__':
    unittest.main()
