import pandas as pd

df=pd.DataFrame({
    "Name": ["Ajmal", "Rahul", "Anu"],
    "Age": [21, 22, 20]

})

print(df)

print(df["Name"])

average_age=df["Age"].mean()
print("average age:",average_age)

oldest_student=df.loc[df["Age"].idxmax()]
print("oldest student:")
print (oldest_student)