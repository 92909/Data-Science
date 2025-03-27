import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from sklearn.model_selection import train_test_split


data1 = pd.read_csv("student_data2.csv")
data2 = pd.DataFrame(data1)
print(data2.head(50))

# lets check if there is any missing values in the dataset
print(data2.isnull().sum()) 
# the data types of the values - Although i had manually changed them to numerical ones earlier
print(data2.dtypes)

# summarizing or describing the dataset
print(data2.describe())

# Now we are moving to the part where we viauslize the datasets, 
# in form of diagrams like bar charts and bar graghs and such
# am not a pro in this region
# lets start with visualizing how the students high school grades were distri uted
#we will use a histogram

sns.histplot(data2["High_School_Grade"], bins=10, kde=True)
plt.title("Distribution of High School Grades")
plt.xlabel("High Schoo,l Grade")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# now lets dreaw a bar chart to show the number of students whoa re enrolled
# versus those who are not enrolled

sns.countplot(x = "Enrolled", data=data2)
plt.title("The number of students enrolled vs the number of students not enrolled distribution")
plt.xlabel("Enrollment Status - 1 => enrolled, 0 => not enrolled")
plt.ylabel("Number of students")
plt.legend()
plt.show()


# there i a column that i need to drop. I included the who need support grduating 
# column yet it should be determined by the model
data2 = data2.drop(columns=["Needs_Graduation_Support"])

# Lets now check to make sure tht there is no duplicates -  and also remove them if there are
print(data2.duplicated().sum())

# lets check the data types of the columns
print(data2.dtypes)
print(data2["Course_Performance_Trend"].unique())


# checking for any correlating values
data2 = data2.drop(columns=['Student_ID'], errors='ignore')  # Adjust column name if different
correlationMatrix = data2.corr()
plt.figure(figsize=(10, 6))
sns.heatmap(correlationMatrix, annot=True, cmap="coolwarm")
plt.title("feature of correlation heat map")
plt.show()


# Now we go to the main part pf the assignment
# the model training
# So forst we are going to split the data in a 80 - 20 % way
X = data2.drop(columns="Enrolled")
y = data2["Enrolled"]

# lets split the data 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 

print("Training set size : ", X_train.shape)
print("Test set size : ", X_test.shape)


# Woooo, to training the model
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)
print("Model Training is complete")


# time to try and make predictions
y_pred = model.predict(X_test)
# this is to print the predictions
print("Predictions : ", y_pred) 
# lets try and orint the real values
print("Real Values : ", y_test.values)

# lets check the accuracy
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)
print("The model accuracy is :", accuracy)



#GIving the reports
from sklearn.metrics import classification_report
report = classification_report(y_test, y_pred)
print("Classification report : ", report)