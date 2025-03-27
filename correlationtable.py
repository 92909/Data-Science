import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

load_data = pd.read_csv("withmissingvalues.csv")
correlationtable = load_data[["StudentID", "Age", "Test Score"]].corr()
print("Correlation table")
print(correlationtable)