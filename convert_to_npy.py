import numpy as np
import matplotlib.pyplot as plt

grid = np.load('pittsburgh.npy')
# grid = grid/255
print(grid.shape)
plt.imshow(grid)
plt.tight_layout()
plt.show()
