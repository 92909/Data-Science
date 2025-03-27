import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x1 = [2,3,4]
y1 = [5,5,5]
x2 = [1,2,3,4,5]
y2 = [6,7,8,4,6]
y3 = [6,8,7,8,6]

plt.scatter(x1,y1, label="GW")
plt.scatter(x2,y2,label="geo", marker="v", color="r")
plt.scatter(x2,y3,label="Kimani", marker="^", color="m")
plt.title("Scatter plot")
plt.legend()
plt.show()
