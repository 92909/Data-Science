import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

months = ['07/2019', '08/2019', '09/2019', '10/2019', '11/2019']
searches = [50, 53, 59, 56, 62]
direct = [39, 47, 42, 51, 51]
social_media = [70, 80, 90, 87, 92]

x = np.arange(len(months))
width = 0.20 

fig, image = plt.subplots(figsize=(8,6))
image.bar(x - width, searches, width, label='Searches', color='blue')
image.bar(x, direct, width, label='Direct', color='pink')
image.bar(x + width, social_media, width, label='Social Media', color='orange')

image.set_xlabel('months')
image.set_ylabel('visitors (in thousands)')
image.set_title('Visitors by web traffic sources')
image.set_xticks(x)
image.set_xticklabels(months)
image.legend(loc='lower right', ncol=3)

plt.show()
