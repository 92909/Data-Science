import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# enter dataset, the file with the information, info_dataset.csv
df = pd.read_csv("Assignment 2/info_dataset.csv", encoding="utf-8")

# defining mapping values to use
road_condition_mapping = {"Good": 0, "Wet": 1, "Damaged": 2}

traffic_volume_mapping = {"Low": 0, "Medium": 1, "High": 2}
accident_severity_mapping = {"Minor": 0, "Serious": 1, "Fatal": 2}

# apply calues to use for mappings 

df["Road Condition"] = df["Road Condition"].map(road_condition_mapping)
df["Traffic Volume"] = df["Traffic Volume"].map(traffic_volume_mapping)
df["Accident Severity"] = df["Accident Severity"].map(accident_severity_mapping)


# droping missing values or null values
df = df.dropna()

# defining the features and te target, ie,  x and y
X = df[["Road Condition", "Traffic Volume", "Vehicles Involved", "Injuries", "Fatalities"]]
y = df["Accident Severity"]


# divising the data into 2 parts, training part or set and testing set


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#lets try to train linear regression model
accident_forecaster = LinearRegression()
accident_forecaster.fit(X_train, y_train)

# trying to make predictions
y_pred = accident_forecaster.predict(X_test)



y_pred_rounded = [round(value) for value in y_pred]

mean_sq_error = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# outputtingg results
print(f"Mean Squared Error: {mean_sq_error}")
print(f"R-squared Score: {r2}")
print("Predicted Accident Severity:", y_pred_rounded[:1000])


results_df = X_test.copy()
results_df["Predicted Severity"] = y_pred_rounded
results_df["Severity Score"] = y_pred
print("\nPredicted Accident Severity with Conditions:\n")
print(results_df)



high_severity_cases = results_df[results_df["Predicted Severity"] >= 2]
low_severity_cases = results_df[results_df["Predicted Severity"] == 0]

# trying to calculate accident trendss
avg_vehicles_high_severity = high_severity_cases["Vehicles Involved"].mean()
avg_fatalities_high_severity = high_severity_cases["Fatalities"].mean()
avg_injuries_high_severity = high_severity_cases["Injuries"].mean()

avg_vehicles_low_severity = low_severity_cases["Vehicles Involved"].mean()
avg_fatalities_low_severity = low_severity_cases["Fatalities"].mean()
avg_injuries_low_severity = low_severity_cases["Injuries"].mean()

print("\n")
print("<h1>Conclusion<h1>")
print(f"severe accidents and fatal category are more likely when road conditions are poor, "
      f"with an average of {avg_vehicles_high_severity:.1f} vehicles involved per accident, "
      f"{avg_injuries_high_severity:.1f} injuries, and {avg_fatalities_high_severity:.1f} fatalities.")
print(f"On the other hand, minor accidents occur more frequently in good conditions, "
      f"averaging {avg_vehicles_low_severity:.1f} vehicles, {avg_injuries_low_severity:.1f} injuries, "
      f"and {avg_fatalities_low_severity:.1f} fatalities.")


print("\n")
print("<h1>Recommendation  <h1>")
if avg_fatalities_high_severity > 0.5:
    print("To reduce fatalities, authorities should improve road conditions, enforce speed limits, and regulate vehicle maintenance.")
if avg_injuries_high_severity > 1.5:
    print("Emergency response systems should be enhanced in high-risk areas to improve survival rates.")
if avg_vehicles_high_severity > 2:
    print("High traffic volume increases accident severity. Implementing better traffic control measures can help reduce collisions.")