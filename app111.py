import pandas as pd

df = pd.DataFrame({
    "Name": ["Ajmal", "Rahul", "Anu", "Sara"],
    "Age": [21, 22, 20, 23],
    "Mark": [85, 72, 95, 68]
})

print(pd)

print(df[["Age","Mark"]])

average_mark=df["Mark"].mean()
print("average mark:",average_mark)

youngest_student=df.loc[df["Age"].idxmin()]
print("younest student:")
print(youngest_student)

students = df[df["Mark"] > 75]
print("Students with mark greater than 75:")
print(students)