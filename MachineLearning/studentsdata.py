import pandas as pd
import numpy as np

# Generating data
np.random.seed(42)

# Creating student names
students = ['Student_A', 'Student_B', 'Student_C', 'Student_D', 'Student_E']

# Generating random grades for each student in different subjects
grades_data = {
    'Math': np.random.randint(0, 100, size=len(students)),
    'Science': np.random.randint(0, 100, size=len(students)),
    'English': np.random.randint(0, 100, size=len(students))
}

# Creating a DataFrame
grades_df = pd.DataFrame(grades_data, index=students)

# Displaying the dataset
print(grades_df)
