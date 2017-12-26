import sys
import math


class AsciiDrawStd:
    width = 30
    xmin = sys.float_info.min
    xmax = sys.float_info.max

    def __init__(self, width):
        self.width = width

    def setXmin(self, xmin):
        self.xmin = xmin

    def setXmax(self, xmax):
        self.xmax = xmax

    def draw_array(self, x):
        dataMax = sys.float_info.min
        dataMin = sys.float_info.max
        for i in range(0, len(x)):
            dataMax = max(dataMax, x[i])
            dataMin = min(dataMin, x[i])

        self.xmin = dataMin
        self.xmax = dataMax

        for i in range(0, len(x)):
            diff = self.xmax - self.xmin

            dirac = 0
            if diff == 0:
                dirac = 1
            else:
                dirac = 0

            s = (1.0 * x[i] - self.xmin) / (diff + dirac)
            print("*" * int(math.floor(s * self.width)))
            print("*")

    def draw_array_with_scale(self, x):
        for i in range(0, len(x)):
            diff = self.xmax - self.xmin
            if diff == 0:
                dirac = 1
            else:
                dirac = 0
            s = (1.0 * x[i] - self.xmin) / (diff + dirac)
            number_of_spaces = int(math.floor(s * self.width))
            my_str = "*" * number_of_spaces
            print(my_str + "*")
