# Data Science Libraries Guide

# Importing data science libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 1. Data Preparation with pandas

# Creating a sample dataset
data = {'X': [1, 2, 3, 4, 5], 'Y': [2, 4, 5, 4, 5]}
df = pd.DataFrame(data)

# Displaying the dataset
print("Original Dataset:")
print(df)

# 2. Data Visualization with matplotlib

# Plotting a scatter plot
plt.scatter(df['X'], df['Y'])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot')
plt.show()

# 3. Simple Linear Regression with scikit-learn

# Splitting the dataset into features (X) and target variable (Y)
X = df[['X']]
Y = df['Y']

# Splitting the dataset into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Creating a linear regression model
model = LinearRegression()

# Training the model
model.fit(X_train, Y_train)

# Making predictions on the test set
Y_pred = model.predict(X_test)

# Evaluating the model
mse = mean_squared_error(Y_test, Y_pred)
print(f"Mean Squared Error: {mse}")

# 4. Displaying Results

# Plotting the regression line
plt.scatter(X_test, Y_test, color='black')
plt.plot(X_test, Y_pred, color='blue', linewidth=3)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression')
plt.show()

# This example briefly covers data preparation with pandas, data visualization with matplotlib, and simple linear regression with scikit-learn. Keep in mind that data science involves a wide range of tasks, and there are many other libraries (e.g., numpy, seaborn, tensorflow, pytorch, etc.) that you may encounter depending on your specific needs.
# Before running the program, you might need to install the required libraries: pip install pandas matplotlib scikit-learn
