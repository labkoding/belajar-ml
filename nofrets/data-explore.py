# 1. Importing the required libraries for EDA
import pandas as pd
import numpy as np
import seaborn as sns                       #visualisation
import matplotlib.pyplot as plt             #visualisation

# 2. Loading the data into the data frame.
df = pd.read_csv("../data.csv")

# To display the top 5 rows 
# print(df.head(5))
# To display the botton 5 rows
# print(df.tail(5))

# 3. Checking the types of data
# print(df.dtypes)

# 4. Dropping irrelevant columns
df = df.drop(['Engine Fuel Type', 'Market Category', 'Vehicle Style', 'Popularity', 'Number of Doors', 'Vehicle Size'], axis=1)
# print(df.head(5))

# 5. Renaming the columns
df = df.rename(columns={"Engine HP": "HP", "Engine Cylinders": "Cylinders", "Transmission Type": "Transmission", "Driven_Wheels": "Drive Mode","highway MPG": "MPG-H", "city mpg": "MPG-C", "MSRP": "Price" })
# print(df.head(5))

# 6. Dropping the duplicate rows
# print(df.shape)
duplicate_rows_df = df[df.duplicated()]
# print("number of duplicate rows: ", duplicate_rows_df.shape)

# print(df.count())

df = df.drop_duplicates()
# print(df.head(5))

# print(df.count())

# 7. Dropping the missing or null values.

# print(df.isnull().sum())
# Dropping the missing values.
df = df.dropna()
# print(df.count())

 # After dropping the values
# print(df.isnull().sum())

# 8. Detecting Outliers
# print(sns.boxplot(x=df['Price']))

# print("done")
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

# print(IQR)

df = df[~((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]
# print(df.shape)


