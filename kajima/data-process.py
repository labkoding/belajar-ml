import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats


#load the data to data frame
df = pd.read_csv("data.csv")

#rename columns
df = df.rename(columns={"Make":"CarBrand","Engine HP": "HP", "Engine Cylinders": "Cylinders", "Transmission Type": "Transmission", "Driven_Wheels": "Drive Mode","highway MPG": "MPG-H", "city mpg": "MPG-C", "MSRP": "Price" })

#dropping duplicate rows
duplicate_rows_df = df[df.duplicated()]
df = df.drop_duplicates()

#dropping outlier
df_after = df[(np.abs(stats.zscore(df['Price'])) < 3)]

#saving to a new csv file
df.to_csv(r'kajima/clean-data.csv')
