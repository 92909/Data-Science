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