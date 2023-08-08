
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import idct

X_all = np.zeros((8*8, 8*8))
for i in range(8):
    for j in range(8):
        # create DCT coefficients
        Y = np.zeros((8, 8), dtype='float64')
        Y[i, j] = 1
        # iDCT 2D
        X = idct(idct(Y, axis=1, norm='ortho'), axis=0, norm='ortho')
        # normalize to [0,1] and store
        X_all[(i*8):((i+1)*8), (j*8):((j+1)*8)] = (X-X.min())/(X.max()-X.min())

fig, ax = plt.subplots(1, 1)
ax.imshow(X_all, cmap='gray', interpolation='nearest', vmin=0, vmax=1)
for i in range(0, 9):
    ax.axvline(i*8-.5, 0, 64, color='cyan')
    ax.axhline(i*8-.5, 0, 64, color='cyan')
plt.axis('off')
fig.savefig('dct.png', dpi=600, bbox_inches='tight')
