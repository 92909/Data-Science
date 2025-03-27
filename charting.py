import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y1 = [1, 3, 5, 3, 1, 3, 5, 3, 1]
y2 = [2, 4, 6, 4, 2, 4, 6, 4, 2]
 
plt.plot(x, y1, label="SEM1")
plt.plot(x,y2, label="SEM2")
plt.plot()

plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("DISTRIBUTION PER SEMESTER")
plt.legend() # this is used to describe the various elements used in various parts prts of the graph
plt.show()