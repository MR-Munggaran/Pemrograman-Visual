import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-8, 8, 10000)
plt.figure(figsize=(6, 4))

y = x - x - 0
y1 = (14 - x**2)**0.5
y2 = -(14 - x**2)**0.5

y3 = 3 + (4 - (x - 3)**2)**0.5
y4 = 3 - (4 - (x - 3)**2)**0.5

y7 = 3 + (4 - (x + 3)**2)**0.5
y8 = 3 - (4 - (x + 3)**2)**0.5

plt.fill_between(x, y7, y8, color='yellow', alpha=1, label='Area Telinga kiri')
plt.fill_between(x, y3, y4, color='green', alpha=1, label='Area Telinga Kanan')
plt.fill_between(x, y1, y2, color='black', alpha=1, label='Area Kepala')


plt.legend(loc='upper center')
plt.grid()
plt.show()
