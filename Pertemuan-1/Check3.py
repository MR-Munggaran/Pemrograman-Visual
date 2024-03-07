print("\033c")       # To close all
import numpy as np
import matplotlib.pyplot as plt

# Optimizing my diagram to the Full HD screen.
row = int(1080)
col = int(1920)

# Defining the top, bottom, left, and right margins for the flag.
# For the black stripe
Brow1 = int(0.25*row)
Brow2 = int(0.5*row)
Bcol1 = 0
Bcol2 = col
# For the red stripe
Rrow1 = int(0.4*row)
Rrow2 = int(0.75*row)
Rcol1 = 0
Rcol2 = col
# For the gold/yellow stripe
Yrow1 = int(0.70*row)
Yrow2 = row
Ycol1 = 0
Ycol2 = col

# Creating the flag image
Gambar = np.zeros(shape=(row, col, 3), dtype=np.int16)

# Filling the black stripe
Gambar[Brow1:Brow2, Bcol1:Bcol2, 0] = 0
Gambar[Brow1:Brow2, Bcol1:Bcol2, 1] = 0
Gambar[Brow1:Brow2, Bcol1:Bcol2, 2] = 0

# Filling the red stripe
Gambar[Rrow1:Rrow2, Rcol1:Rcol2, 0] = 255
Gambar[Rrow1:Rrow2, Rcol1:Rcol2, 1] = 0
Gambar[Rrow1:Rrow2, Rcol1:Rcol2, 2] = 0

# Filling the gold/yellow stripe
Gambar[Yrow1:Yrow2, Ycol1:Ycol2, 0] = 255
Gambar[Yrow1:Yrow2, Ycol1:Ycol2, 1] = 255
Gambar[Yrow1:Yrow2, Ycol1:Ycol2, 2] = 0

plt.figure()
plt.imshow(Gambar)
plt.show()
