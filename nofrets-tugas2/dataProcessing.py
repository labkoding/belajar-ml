import pandas as pd
import numpy as np
import seaborn as sns                       #visualisation
import matplotlib.pyplot as plt             #visualisation

# load file data.csv
df = pd.read_csv("../data.csv")

# 1. rename kolom
df = df.rename(columns={"Engine HP": "HP", "Engine Cylinders": "Cylinders", "Transmission Type": "Transmission", "Driven_Wheels": "Drive Mode","highway MPG": "MPG-H", "city mpg": "MPG-C", "MSRP": "Price" })

# 2. hapus data duplikat

# 3. hapus data outlier

# save ke file yang baru (data_clean.csv)


