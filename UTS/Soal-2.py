import numpy as np
import matplotlib.pyplot as plt

x = np.linspace (-8,8,10000)
plt.figure(figsize=(8,6.5))

y1 = (25-x**2)**0.5
y2 = -(25-x**2)**0.5

y3 = 4 + (4-(x-4)**2)**0.5
y4 = 4 - (4-(x-4)**2)**0.5

y5 = -4 + (4-(x-4)**2)**0.5
y6 = -4 - (4-(x-4)**2)**0.5

y7 = 6 + (4-(x+0)**2)**0.5
y8 = 6 - (4-(x+0)**2)**0.5

y9 = -6 + (4-(x+0)**2)**0.5
y10 = -6 - (4-(x+0)**2)**0.5

y11 = 4 + (4-(x+4)**2)**0.5
y12 = 4 - (4-(x+4)**2)**0.5

y13 = -4 + (4-(x+4)**2)**0.5
y14 = -4 - (4-(x+4)**2)**0.5

y15 = 0 + (4-(x-5)**2)**0.5
y16 = 0 - (4-(x-5)**2)**0.5

y17 = 0 + (4-(x+5)**2)**0.5
y18 = 0 - (4-(x+5)**2)**0.5


plt.plot(x, y1, '-r', label='y1, y2')
plt.plot(x, y2, '-r')
plt.plot(x, y3, '-b', label='y3, y4')
plt.plot(x, y4, '-b')
plt.plot(x, y5, '-b', label='y5, y6')
plt.plot(x, y6, '-b')
plt.plot(x, y7, '-b', label='y7, y8')
plt.plot(x, y8, '-b')
plt.plot(x, y9, '-b', label='y9, y10')
plt.plot(x, y10, '-b')
plt.plot(x, y11, '-b', label='y11, y12')
plt.plot(x, y12, '-b')
plt.plot(x, y13, '-b', label='y13, y14')
plt.plot(x, y14, '-b')
plt.plot(x, y15, '-b', label='y13, y14')
plt.plot(x, y16, '-b')
plt.plot(x, y17, '-b', label='y13, y14')
plt.plot(x, y18, '-b')


plt.fill_between(x, y1, y2, color='red', alpha=0.1)
plt.fill_between(x, y3, y4, color='pink', alpha=1)
plt.fill_between(x, y5, y6, color='pink', alpha=1)
plt.fill_between(x, y7, y8, color='pink', alpha=1)
plt.fill_between(x, y9, y10, color='pink', alpha=1)
plt.fill_between(x, y11, y12, color='pink', alpha=1)
plt.fill_between(x, y13, y14, color='pink', alpha=1)
plt.fill_between(x, y15, y16, color='pink', alpha=1)
plt.fill_between(x, y17, y18, color='pink', alpha=1)

plt.legend()
plt.grid()
plt.show()