import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 2.5, 3, 5]
y = [1, 4, 6, 9 , 13]
plt.plot(x, y, 'ro')
plt.axis([0, 6, 0, 20])

plt.plot(np.unique(x), np.poly1d(np.polyfit(x,y,1))(np.unique(x)))
plt.show()