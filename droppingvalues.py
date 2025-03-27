
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

# suppose we want to remove the age part
df = pd.DataFrame(data)
print(df)

no_valid = 0
averaged = 0
for mark in df['Marks']:
    if str(mark).isnumeric():
        no_valid = no_valid + 1
        averaged = averaged + mark

average = averaged / no_valid
print(average)
df = df.replace(to_replace='NaN', value=average)


df = df[df['Marks'] >= 80]
df = df.drop(['age'], axis=1)
print(df)


# now, suppose you want to output the best 3 students in rhe group
df.sort_values(by='Marks', ascending=False, inplace=True)
top_scorers = df[['Name', 'Gender', 'Marks']].head(3)
print(top_scorers)