"""
📘 Day 25: Pandas (Python Data Analysis Library)

Pandas is used to:
• Read data files (CSV, Excel, JSON)
• Work with tables of data (rows & columns)
• Clean, analyze, and explore data

Very common in:
• Cloud engineering
• Data pipelines
• Logging & monitoring
• AI / ML preprocessing
"""

# ---------------------------------------------------
# IMPORTING PANDAS
# ---------------------------------------------------

import pandas as pd
# Convention: pandas is always imported as "pd"


# ---------------------------------------------------
# READING A CSV FILE
# ---------------------------------------------------

# File path to CSV
file_path = "/Users/zoniquefoyle/Downloads/countries of the world.csv"

# Read CSV into a DataFrame
df = pd.read_csv(file_path)

print("✅ CSV loaded successfully!")

# Shape = (rows, columns)
print("Rows, Columns:", df.shape)

# Show first 5 rows
print("\nFirst 5 rows:")
print(df.head())


# ---------------------------------------------------
# BASIC DATAFRAME EXPLORATION (VERY IMPORTANT)
# ---------------------------------------------------

# Show column names
print("\nColumn names:")
print(df.columns)

# Show data types and missing values
print("\nDataFrame info:")
print(df.info())


# ---------------------------------------------------
# CLEANING TEXT DATA (REAL-WORLD SKILL)
# ---------------------------------------------------

# Remove extra spaces from text columns
df["Country"] = df["Country"].str.strip()
df["Region"] = df["Region"].str.strip()

print("\n✅ Cleaned text columns")

# Save cleaned file
df.to_csv("countries_cleaned.csv", index=False)
print("✅ Saved cleaned CSV as countries_cleaned.csv")


# ---------------------------------------------------
# PANDAS SERIES
# ---------------------------------------------------

"""
A Pandas Series is:
• A one-dimensional data structure
• Similar to a list, but with labels (index)
"""

# Creating Pandas Series with default index
nums = [1, 2, 3, 4, 5]
s = pd.Series(nums)

print("\nPandas Series (default index):")
print(s)


# Creating Pandas Series with custom index
nums = [1, 2, 3, 4, 5]
s = pd.Series(nums, index=[1, 2, 3, 4, 5])

print("\nPandas Series (custom index):")
print(s)


# ---------------------------------------------------
# WHY THIS MATTERS FOR CLOUD / AWS
# ---------------------------------------------------

"""
Real-world use cases:
• Reading logs from CSV files
• Analyzing cost reports
• Processing monitoring data
• Preparing data before uploading to S3
• Feeding data into ML models
"
"""
