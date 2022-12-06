from operator import index
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

df = df.rename(columns={"Engine HP": "HP", "Engine Cylinders": "Cylinders", "Transmission Type": "Transmission", "Driven_Wheels": "Drive Mode","highway MPG": "MPG-H", "city mpg": "MPG-C", "MSRP": "Price" })

df = df.drop_duplicates()
print(df.head(5))

print(sns.boxplot(x=df['Price']))

df.to_csv('Fandescho.csv', index=False)