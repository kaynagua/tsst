import matplotlib.pyplot as plt
import numpy as np
########################
x = np.array(["A","E","I","O","U"])
y = np.array([10,-20,30,-40,50])
############
plt.bar(x, y, width = 0.5)
plt.show()