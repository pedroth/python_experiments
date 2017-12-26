import math
import matplotlib.pyplot as plt


class Complex:
    def __init__(self, x, y):
        assert isinstance(x, (int, float)) and isinstance(y, (int, float))
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def add(self, z):
        assert isinstance(z, Complex) or isinstance(z, (int, float))
        if isinstance(z, Complex):
            return Complex(self.x + z.x, self.y + z.y)
        return Complex(self.x + z, self.y)

    def diff(self, z):
        assert isinstance(z, Complex) or isinstance(z, (int, float))
        if isinstance(z, Complex):
            return Complex(self.x - z.x, self.y - z.y)
        return Complex(self.x - z, self.y)

    def prod(self, z):
        assert isinstance(z, Complex) or isinstance(z, (int, float))
        if isinstance(z, Complex):
            return Complex(self.x * z.x - self.y * z.y, self.y * z.x + self.x * z.y)
        return Complex(self.x * z, self.y * z)

    def square_norm(self):
        return self.x * self.x + self.y * self.y

    def norm(self):
        return math.sqrt(self.square_norm())

    def conj(self):
        return Complex(self.x, self.y)

    def div(self, z):
        assert isinstance(z, Complex) or isinstance(z, (int, float))
        if isinstance(z, Complex):
            return self.prod(z.conj()).prod(1 / z.square_norm())
        return Complex(self.x / z, self.y / z)

    def __str__(self):
        return str(self.x) + " + i" + str(self.y)

    def to_tuple(self):
        return self.x, self.y,

    def transform(self, f):
        return f(self)

    def __mul__(self, z):
        return self.prod(z)

    def __add__(self, z):
        return self.add(z)

    def __sub__(self, z):
        return self.diff(z)

    def __truediv__(self, z):
        return self.div(z)


z1 = Complex(1, 0)
z2 = Complex(0, 1)

print(z1.add(z2))
print(z1.prod(z2))
print(z1.div(z2))

print(z1 + z2)
print(z1 * z2)
print(z1 / z2)

print(z1 / z2 - z1.div(z2))

p = lambda z: z.prod(z).add(1)

print(z1.transform(p))


def createGrid(min_oomplex, max_complex, samples):
    assert len(samples) == 2 and isinstance(min_oomplex, Complex) and isinstance(max_complex, Complex)
    matrix = []
    stepX = (max_complex.x - min_oomplex.x) / (samples[0] - 1)
    stepY = (max_complex.y - min_oomplex.y) / (samples[1] - 1)
    for i in range(samples[0]):
        new_matrix = []
        for j in range(samples[1]):
            new_matrix.append(Complex(min_oomplex.x + stepX * i, min_oomplex.y + stepY * j))
        matrix.append(new_matrix)
    # matrix = [[Complex(min_oomplex.x + stepX * i, min_oomplex.y + stepY * j) for j in range(samples[1])] for i in range(samples[0])]
    return matrix


grid = createGrid(Complex(0, 0), Complex(1, 1), [10, 10])
for z in grid:
    print(" ".join(map(str, z)))

f, (ax1, ax2) = plt.subplots(1, 2)
for line in grid:
    for z in line:
        ax1.scatter(z.x, z.y)
        w = z.transform(p)
        ax2.scatter(w.x, w.y)
plt.show()

