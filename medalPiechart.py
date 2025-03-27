import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

medals = pd.read_csv("medal.csv")
country_data = medals["country"]
medal_data = medals["gold_medal"]
colors = "r", "y", "b", "b", "g"
plt.pie(medal_data, labels=country_data, colors=colors, autopct="%.2f%%")
plt.title("Gold medals winnings by different countries")
plt.legend()
plt.show()