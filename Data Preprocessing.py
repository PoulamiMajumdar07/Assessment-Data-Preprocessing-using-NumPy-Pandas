#Data Preprocessing


# Fill numeric missing values with column mean
numeric_cols = df.select_dtypes(include=np.number).columns

for col in numeric_cols:
    df[col].fillna(df[col].mean(), inplace=True)

# Fill categorical missing values with mode
categorical_cols = df.select_dtypes(include='object').columns

for col in categorical_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

print("\nMissing Values Handled!")

# Convert exam_date to datetime format
df['exam_date'] = pd.to_datetime(df['exam_date'], errors='coerce')

print("\nExam Date Converted to Datetime!")

# Convert incorrect formats if needed
df['attendance'] = pd.to_numeric(df['attendance'], errors='coerce')

def remove_outliers(dataframe, column):
    Q1 = dataframe[column].quantile(0.25)
    Q3 = dataframe[column].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    return dataframe[
        (dataframe[column] >= lower) &
        (dataframe[column] <= upper)
    ]

# Remove outliers
df = remove_outliers(df, 'math_score')
df = remove_outliers(df, 'science_score')

print("\nOutliers Removed!")

# Remove duplicate rows
df.drop_duplicates(inplace=True)

print("\nDuplicate Rows Removed!")
