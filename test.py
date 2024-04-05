import PyQt6

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2*np.pi,2*np.pi,0.01)
y = np.sin(3*x)/x
plt.plot(x,y)
plt.show()


