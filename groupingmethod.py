import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt

STUDENTDETAILS = {
    'IDNO': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'NAME': ['Peter', 'Joyce', 'George', 'Phylis', 'Moses', 'Priscillah', 'Eliud', 'Veronicah', 'John', 'Juliet'],
    'Campus': ['Main', 'Ruiru', 'Nairobi', 'Main', 'Ruiru', 'Nairobi', 'Main', 'Ruiru', 'Nairobi', 'Main']
}

data1 = pd.DataFrame(STUDENTDETAILS)
print(data1)


FEESDETAILS = {
    'IDNO': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'PENDING': [6000, 375, 0, 7640, 3800, 0, 1250, 900, 5200, 0]
}

data2 = pd.DataFrame(FEESDETAILS)
print(data2)

# now, lets try merging them
merged_dataframe = pd.merge(data1, data2, on='IDNO')
print(merged_dataframe)

# lets group them based on campus
grouped_dataframe = merged_dataframe.groupby('Campus')['PENDING'].sum().reset_index()
print("The total pending fees per campus is : ")
print(grouped_dataframe)