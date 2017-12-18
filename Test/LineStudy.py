import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("resources/lines.png")
height = img.shape[0]
width = img.shape[1]
bw = np.zeros([width, height])
nn = width * height
for t in range(nn):
    j = t % width
    i = t // width
    np_sum = sum(img[i, j])
    bw[i, j] = 1 if np_sum > 0 else 0

plt.matshow(bw)
fig, ax = plt.subplots()
hist = np.sum(bw, axis=1)
ax.plot(range(width), hist, 'r-', linewidth=2)
plt.show()

np.save('resources/lineHist', hist)
