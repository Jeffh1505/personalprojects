import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
# Generating data for 100 students
np.random.seed(42)

# Creating student names
students = [f"Student_{i}" for i in range(1, 1001)]

# Generating random grades for each student in different subjects
grades_data = {
    'Math': np.random.randint(50, 100, size=len(students)),
    'Science': np.random.randint(50, 100, size=len(students)),
    'English': np.random.randint(50, 100, size=len(students))
}

# Creating a DataFrame
grades_df = pd.DataFrame(grades_data, index=students)

# Displaying the first few rows of the dataset
print(grades_df)
#print(grades_df.describe())



# Assuming grades_df contains the dataset with grades and the target variable (at-risk or not at-risk)
# Define at-risk based on a threshold, for example, a GPA less than 70
grades_df['At_Risk'] = grades_df[['Math', 'Science', 'English']].mean(axis=1) < 70

# Features (X) and target variable (y)
X = grades_df[['Math', 'Science', 'English']]
y = grades_df['At_Risk']

# Splitting the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initializing and training the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
print(y_pred)

# Evaluation
print(classification_report(y_test, y_pred))
