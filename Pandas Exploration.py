#Pandas Exploration


# Display first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Data types
print("\nData Types:")
print(df.dtypes)

# Missing values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# Students with attendance below 70%
print("\nStudents with Attendance Below 70%:")
low_attendance = df[df['attendance'] < 70]
print(low_attendance)
