import pandas as pd
df=pd.read_csv("students1.csv")

df["Total"] = df["Math"] + df["Science"] + df["English"]


df["Average"] = df["Total"] / 3

def grade (mark):
    if mark >= 90:
        return "A"
    elif mark>=80:
        return "B"
    elif mark>=70:
        return "C"
    elif mark>=60:
        return "D"
    else :
        return "F"

df["Grade"] = df["Average"].apply(grade)

df["Result"] = df["Average"].apply(
    lambda x: "Pass" if x >= 50 else "Fail")

class_Avarage= df ["Average"].mean()

top_student= df.loc[df["Total"].idxmax()]

pass_percentage = (df["Result"] == "Pass").mean() * 100

print(df)

print("class Avarage:",class_Avarage)
print(top_student)
print("pass percentage:",pass_percentage)