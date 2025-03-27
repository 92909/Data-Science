import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

datas = pd.read_csv("medal.csv")
country_data = datas["country"]
medal_data = datas["gold_medal"]

#plotting the line graph
plt.plot(country_data, medal_data, label="Distribution", color="r")
plt.plot()

plt.xlabel("Country Data")
plt.ylabel("Medal Data")
plt.title("The Distribution of gold medals in different countries")
plt.legend()
plt.show()
