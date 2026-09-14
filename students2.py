# import pandas as pd

# df=pd.read_csv("students.csv")
# df["Total"] = df["malayalam"] + df["english"] + df["science"]
# print(df)

import pandas as pd
df=pd.read_csv("students.csv")
df["total"]=df["malayalam"]+df["english"]+df["science"]
print(df)