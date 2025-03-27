import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

labels = "A", "B", "C"
colors = ["g", "r", "y"]
sections = [56, 73, 32]
plt.pie(sections, labels=labels, colors=colors, startangle=90,autopct = '%1.2f%%') # am not sure 
#what the last part is
plt.title("Grades of 3 Sciemces")
plt.legend()
plt.show()