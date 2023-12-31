import pandas as pd
import numpy as np

# Generating data for 100 students
np.random.seed(42)

# Creating student names
students = [f"Student_{i}" for i in range(1, 101)]

# Generating random grades for each student in different subjects
grades_data = {
    'Math': np.random.randint(60, 100, size=100),
    'Science': np.random.randint(60, 100, size=100),
    'English': np.random.randint(60, 100, size=100)
}

# Creating a DataFrame
grades_df = pd.DataFrame(grades_data, index=students)

# Displaying the first few rows of the dataset
print(grades_df.head())
