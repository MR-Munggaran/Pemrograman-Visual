import matplotlib;matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cv2
import time

import matplotlib.animation as animation

fig, ax = plt.subplots()
t = np.linspace(0, 3, 40)
g = -9.81
v0 = 12
z = g * t**2 / 2 + v0 * t

v02 = 5
z2 = g * t**2 / 2 + v02 * t

scat = ax.scatter(t[0], z[0], c="b", s=5, label=f'v0 = {v0} m/s')
line2 = ax.plot(t[0], z2[0], label=f'v0 = {v02} m/s')[0]
ax.set(xlim=[0, 3], ylim=[-4, 10], xlabel='Time [s]', ylabel='Z [m]')
ax.legend()


def update(frame):
    # for each frame, update the data stored on each artist.
    x = t[:frame]
    y = z[:frame]
    # update the scatter plot:
    data = np.stack([x, y]).T
    scat.set_offsets(data)
    # update the line plot:
    line2.set_xdata(t[:frame])
    line2.set_ydata(z2[:frame])
    return (scat, line2)


ani = animation.FuncAnimation(fig=fig, func=update, frames=40, interval=30)

plt.show()

# tentukan wilayah diagaram cartesian dan rasio lebar dan tinggi diagram
x = np.linspace(-10,10,1000)
plt.figure(figsize=(4,15))

# draw a small cirdcle at (0,0)
plt.plot(x, (0.05 - x*2)* 0.5,    '-k')
plt.plot(x, ((0.05 - x*2)*0.5),  '-k')

# Tentukan persamaan matematika yang diingnakn
y1 = x - x - 0
y2 = 0.5 * x
y3 = x
y4 = 2*x
y5 = -0.5 * x
y6 = -x
y7 = -2*x

plt.plot(x, y1, '-k', label='y1')
plt.plot(x, y2, '-r', label='y2')
plt.plot(x, y3, '-g', label='y3')
plt.plot(x, y4, '-b', label='y4')
plt.plot(x, y5, '-y', label='y5')
plt.plot(x, y6, '-m', label='y6')
plt.plot(x, y7, '-c', label='y7')

plt.legend(loc='upper left')
plt.grid()
plt.show()