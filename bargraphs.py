import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x1 = ["BSCIT", "S.E", "BCE", "BBIT", "BIRD", "EDUC"]
y1 = [200, 300, 250, 150, 250, 450]
plt.bar(x1, y1, label="Yellow bar", color="y")
plt.plot()
plt.xlabel("Course")
plt.ylabel("Number of students")
plt.title("Intake of Different Courses")
plt.legend() # as usual
plt.show()