import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

datasets = pd.read_csv("studentsdata.csv")
print(datasets.head(10))

# duplicating rows or checking for them
duplicate_rows = datasets[datasets.duplicated()]
print("Duplicate Rows")
print(duplicate_rows)
#it returns an empty DATAFRAME since there is no duplicate 
#you can also check per row = dataset[datasets["studentID"].duplicated()]

# now to checking, finding and replacing all the null values
null_values = datasets.isnull().sum()
print("Null Values")
print(null_values)