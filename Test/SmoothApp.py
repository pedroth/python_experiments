import time

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

from LineLaplacianBuilder import get_line_laplacian_eigen
from MatrixExp import matrix_exp_eigen

from Signal1DUtils import find_local_max

global oldTime
oldTime = time.time()
global app_time
app_time = 0

signal = np.load("resources/lineHist.npy")
dim = signal.shape[0]
U, s = get_line_laplacian_eigen(dim)
# signal = np.random.rand(dim)

fig, ax = plt.subplots()
line, = ax.plot(range(dim), signal, 'r-', linewidth=2)
ax.set_xlim([0, dim])
ax.set_ylim([0, 3 * max(signal)])


def data_gen():
    i = 0
    while True:
        i += 1
        yield i


def get_app_time():
    global oldTime
    global app_time
    dt = time.time() - oldTime
    oldTime = time.time()
    app_time += dt
    return app_time, dt


def run(i):
    # clear screen
    ax.clear()

    # get time data
    t, dt = get_app_time()
    print("n : " + str(i) + " t : " + str(t) + " dt : " + str(dt))

    # smoothing signal
    smoothed_signal = matrix_exp_eigen(U, -s, t, signal)

    length = smoothed_signal.shape[0]
    max_signal = max(smoothed_signal)

    # set camera
    ax.set_xlim([0, length])
    ax.set_ylim([0, 2 * max_signal])

    # draw smoothing function
    ax.plot(range(length), smoothed_signal, 'r-', linewidth=2)

    # draw info
    ax.text(.5, 1.05, "heat time = " + str(t), transform=ax.transAxes, va='center')

    # find local maxima and plot it as stem graph
    local = find_local_max(smoothed_signal)
    dim = local.shape[0]
    local_x = np.array(range(dim))
    local_x = local_x[local]
    ones = np.array([1 for x in range(dim)])
    ax.stem(local_x, max_signal * ones[local])


def save_gif(ani):
    Writer = animation.writers['ffmpeg']
    writer = Writer(bitrate=1800)
    ani.save('resources/line.mp4', dpi=80, writer=writer)


if __name__ == "__main__":
    is_video = True
    # time between frames computed by experiment (check dt in logs - average of dt's)
    time_between_frames = 0.1
    time_in_video_seconds = 100

    generator = np.math.floor(time_in_video_seconds / time_between_frames) if is_video else data_gen

    anim = animation.FuncAnimation(fig, run, frames=generator, blit=False, interval=1, repeat=False)
    if is_video:
        save_gif(anim)
    else:
        plt.show()
