import numpy as np
import pandas as pd
df = pd.read_csv("students.csv")
print("Dataset Loaded Successfully!\n")


#NumPy Operations


# Create NumPy array from math_score column
math_scores = np.array(df['math_score'])

print("Math Score Array:")
print(math_scores)

# Mean, Median, Maximum, Minimum
print("\nStatistics:")
print("Mean:", np.mean(math_scores))
print("Median:", np.median(math_scores))
print("Maximum:", np.max(math_scores))
print("Minimum:", np.min(math_scores))

# Normalize Scores
normalized_scores = (math_scores - np.min(math_scores)) / (
    np.max(math_scores) - np.min(math_scores)
)

print("\nNormalized Scores:")
print(normalized_scores)
