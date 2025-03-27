import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt  

coordinates = pd.read_csv("coordinates.csv")
x = coordinates["x"]
y = coordinates["y"]
print(np.mean(x)) # just testing the mean function 
plt.plot(x, y)  
plt.xlabel("X-axis")  
plt.ylabel("Y-axis")  
plt.title("Graph of y = x²")  
plt.grid()  
plt.show()  
