import pandas as pd


df = pd.DataFrame({
    "Name": ["Ajmal", "Rahul", "Anu", "Sara"],
    "Math": [85, 70, 95, 60],
    "Science": [90, 75, 92, 65],
    "English": [80, 80, 90, 70]
})


print(df)
print(df["Name"])
average_mark=df["Science"].mean()
print("averge mark:",average_mark)

highest_mark=df.loc[df["Math"].idxmax()]
print("highest mark:")
print(highest_mark)



