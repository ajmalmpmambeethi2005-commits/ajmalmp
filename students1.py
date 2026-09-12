import pandas as pd

df = pd.read_csv("students.csv")

for index, row in df.iterrows():
    print(row["Name"], row["Marks"])