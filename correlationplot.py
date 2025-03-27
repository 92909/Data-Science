import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

load_data = pd.read_csv("withmissingvalues.csv")
print(load_data.head())

corr_matrix = load_data.select_dtypes(include=[np.number]).corr()

sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation plot of my data")
plt.show()