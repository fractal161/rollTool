import cv2
import numpy as np

tileset = np.zeros((128, 128, 3), np.uint8)

# for simplicity, lowest bits go first (easy enough to reverse)
for i in range(256):
    bits = i
    row = i >> 4
    col = i & 15
    for j in range(8):
        bit = i & (1 << j)
        if bit > 0:
            tileset[8*row:8*(row+1),8*col+j] = (0x55, 0x55, 0x55)



cv2.imwrite('chr/hz.png', tileset)
