import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

load_data = pd.read_csv("withmissingvalues.csv")
print(load_data.head())

plt.boxplot(load_data["StudentID"], vert=False)
plt.title("A Quick Box Plot of Age")
plt.xlabel("Age")
plt.legend()
plt.show()