print("\033c")       # To close all
import numpy as np
import matplotlib.pyplot as plt

# Optimizing my diagram to the Full HD screen.
row = int(800)
col = int(1400)

# Defining the top, bottom, left, and right margins for the flag.
Rrow1 = round(row/8*2)
Rrow2 = round(row/8*3)
Rrow3 = round(row/8*6)
Rcol1 = round(col/14*3)
Rcol2 = round(col/14*11)

# Creating the flag image
Gambar = np.zeros(shape=(row, col, 3), dtype=np.int16)

# Filling the red stripe
Gambar[Rrow1:Rrow2+1, Rcol1:Rcol2+1, :] = [50,50,100]
Gambar[Rrow2:Rrow3+1, Rcol1:Rcol2+1, :] = [80,80,200]

plt.figure()
plt.imshow(Gambar)
plt.show()
