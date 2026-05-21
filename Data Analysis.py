#Data Analysis


# Create average_score column
df['average_score'] = (
    df['math_score'] +
    df['science_score']
) / 2

print("\nAverage Score Column Added!")

# Top 5 students based on average_score
top_students = df.sort_values(
    by='average_score',
    ascending=False
).head(5)

print("\nTop 5 Students:")
print(top_students)

# Correlation between attendance and marks
correlation = df[['attendance', 'math_score', 'science_score']].corr()

print("\nCorrelation Matrix:")
print(correlation)

# Group by gender and calculate average marks
grouped = df.groupby('gender')[[
    'math_score',
    'science_score',
    'average_score'
]].mean()

print("\nAverage Marks by Gender:")
print(grouped)
print("\nFinal Cleaned Dataset:")
print(df.head())
