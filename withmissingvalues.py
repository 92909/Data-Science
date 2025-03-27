import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

load_data = pd.read_csv("withmissingvalues.csv")
print(load_data.head())

# checking the null values now
null_valuess = load_data.isnull().sum()
print("Null Values")
print(null_valuess)

#now we try to fill the NaN or null values using fillna() function
filled_data = load_data.fillna(0)
print("Datasets with missing values replaced")
print(filled_data) # the missing values were replaced by 0

# modifying the value of a specific location
print("Original Dataset")
print(load_data.head(10))
print("Lets change it")
rowindex = 2
columnname = "Test Score"
newvalue = 88
load_data.at[rowindex, columnname] = newvalue
print("Modified dataFrame")
print(load_data)
#lets describe the data
print("Describing the data")
print(load_data.describe())

print("Information")
print(load_data.info())

#counting
print("Unique values gender column")
print(load_data["Gender"].value_counts()) # this counts the number of males and the number of females 

#now we need to represent the number of nstudents with a certain age
# a bar graph
column_name = "Age"
age_counts = load_data["Age"].value_counts()

age_counts.plot(kind='bar', color='gold')
plt.title("The number of students at a certain age")
plt.xlabel(column_name)
plt.ylabel("Count")
plt.legend()

plt.show()

# lets try to get the datatypes of each column
df = pd.DataFrame(load_data)
data_types = df.dtypes
print("The data types of different Dataframe columns are")
print(data_types)

#filtering data
filtered_data = load_data[load_data["Test Score"] > 90]
print("Students who got mpore than 90 are:")
print(filtered_data)