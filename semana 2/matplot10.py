import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.plot([1,2,3],[2,4,6])

x=[0,1,2,3,4]
y=[0,2,4,6,8]

plt.plot(x,y, 'b^--', label="2x")

x2 = np.arange(0,4.5,0.5)
plt.plot(x2, x2**2, "r", label="x^2")


plt.title("Our first Graph!", fontdict={"fontname" : "Comic Sans MS", "fontsize" : 20})
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.xticks([0,1,2,3,4])

plt.legend()

plt.plot(show)