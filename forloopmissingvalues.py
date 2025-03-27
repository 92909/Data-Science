import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data = {
    'Name': ['Kim', 'Jackson', 'Michael', 'Jane', 'Patrick', 'Esther', 'Johnson'],
    'age' : [22, 52, 23, 22, 21, 37, 24],
    'Gender' : ['Male', 'Male', 'Male', 'Female', 'Male', 'Female', 'Male'],
    'Marks' : [85, 92, 'NaN', 88, 'NaN', 79, 80]
}

df = pd.DataFrame(data)
print(df)

valid_marks = 0
total_valid_marks = 0

for mark in df["Marks"]:
    if str(mark).isnumeric():
        valid_marks = valid_marks + 1
        total_valid_marks = total_valid_marks + mark
        
average_marks = total_valid_marks / valid_marks
df = df.replace(to_replace="NaN", value=average_marks)
print("\n New data \n")
print(df)

# in the GENDER column, we can reshape the data by categorizing them into different numbers.
print(df['Gender'].dtype)
# lets change male to 1 and female to 0
df['Gender'] = df['Gender'].map({'Male' : 1 , 'Female' : 0}).astype(float)
print(df)
print(df['Gender'])
# on the above issue, instead of mapping, you can also replace the data
df['Gender'] = df['Gender'].replace({'Male' : 1, 'Female' : 0}).astype(float)
print(df)