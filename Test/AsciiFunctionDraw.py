import math
import DataAsciiDraw


def function_plot(xmin, xmax, f, samples):
    plotter = DataAsciiDraw.AsciiDrawStd(100)
    plotter.setXmin(-1)
    plotter.setXmax(1)
    data = []
    for i in range(0, samples):
        x = xmin + ((xmax - xmin) / (samples - 1)) * i
        value = f(x)
        data.append(value)
    plotter.draw_array_with_scale(data)


function_plot(0, 2 * math.pi, math.sin, 1000)
