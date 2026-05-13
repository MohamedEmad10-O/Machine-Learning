from ctypes.wintypes import PINT
import pandas as pd 

data = [10, 12, 15, 14, 9, 8, 20, 25, 22, 100, 2]

df = pd.DataFrame({"Rainfall" : data})

print(df.head())

Q1 = df['Rainfall'].quantile(.25)
Q3 = df['Rainfall'].quantile(.75)

IQR = Q3 - Q1

Lower_fence = Q1 - 1.5 * IQR
Upper_fence = Q3 + 1.5 * IQR

for x in df['Rainfall']:
    Outliers = (x < Lower_fence) or (x > Upper_fence)
    if Outliers:
                print("Outlier:", x)
                