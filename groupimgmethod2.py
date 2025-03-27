import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt

import pandas as pd

cardata = {
    'Brand': ['Maruti', 'Toyota', 'Mahindra', 'Ford', 'Maruti', 'Toyota', 'Toyota', 'Ford', 'Mahindra', 'Maruti'],
    'Year': [2009, 2010, 2011, 2010, 2010, 2009, 2010, 2012, 2010, 2009],
    'Model': ['Swift', 'Corolla', 'Scorpio', 'Fiesta', 'Alto', 'Camry', 'Innova', 'Figo', 'Bolero', 'WagonR'],
    'Sales': [120, 150, 95, 50, 105, 130, 90, 75, 85, 115]
}

df = pd.DataFrame(cardata)
print(df)
print("Grouped data 2009")
grouped_data = df.groupby("Year")
print(grouped_data.get_group(2009))
print("Grouped data 2010")
print(grouped_data.get_group(2010))

#multiple years
print("Multiple years grouped data")
mychoice = [2011, 2012]
for year in mychoice:
    print(f"\n Data for year {year} \n")
    print(grouped_data.get_group(year))
  
   
#also we can use & operators
sales2010 = df[(df['Year'] == 2010) & (df['Sales'] > 100)]
print(sales2010)

# lets use | operator
sales2011 = df[(df['Year'] == 2010) | (df['Year'] == 2011)]
print(sales2011)