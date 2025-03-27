import pandas as pd
import matplotlib.pyplot as plt

# Creating the dataset
data = {
    "Employee": ["Emily Johnson", "Benjamin Smith", "Sophia Williams", "William Brown", "Olivia Davis", "James Wilson", "Ava Martinez", "Liam Anderson", "Mia Thompson", "Ethan Rodriguez", "Isabella Garcia", "Noah Martinez", "Emma Johnson", "Michael Lee", "Harper Taylor"],
    "Gender": ["Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female"],
    "Department": ["Human Resources", "Marketing", "Finance", "IT", "Sales", "Human Resources", "Marketing", "Finance", "IT", "Sales", "Human Resources", "Marketing", "Finance", "IT", "Sales"],
    "Salary": [6747, 1011, 2109, 1260, 2583, 8284, 3989, 7416, 7625, 7054, 4522, 2028, 8770, 5708, 7693]
}

df = pd.DataFrame(data)

# Line Graph (salaary by employee)
plt.figure(figsize=(10, 5))
plt.plot(df['Employee'], df['Salary'], marker='o', linestyle='-', color='b', label='Salary')
plt.xticks(rotation=90)
plt.xlabel("Employee")
plt.ylabel("Salary")
plt.title("Salary of Employees - Line Graph")
plt.legend()
plt.show()

# Bar Chart (salary by employee)
plt.figure(figsize=(10, 5))
plt.bar(df['Employee'], df['Salary'], color='g')
plt.xticks(rotation=90)
plt.xlabel("Employee")
plt.ylabel("Salary")
plt.title("Salary of Employees - Bar Chart")
plt.show()

# Bar Chart of Salary by Department
department_salary = df.groupby('Department')['Salary'].sum()
plt.figure(figsize=(8, 5))
department_salary.plot(kind='bar', color='purple')
plt.xlabel("Department")
plt.ylabel("Total Salary")
plt.title("Total Salary by Department")
plt.show()
