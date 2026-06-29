import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([10,20, 30, 40, 50])

plt.title("My Graph")
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.plot(x, y, marker = "o", ms=20, mec="red", mfc="red", color="yellow", 
         linewidth=10, linestyle="dotted")
plt.show()


x = np.array(["a","b", "c","d", "e"])
y1 = np.array([1,2,3,4,5])
y2 = np.array([10,20, 30, 40, 50])

plt.plot(x,y1)
plt.plot(x,y2)

plt.show()
