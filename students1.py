# import pandas as pd

# mf=pd.read_csv("student.csv")

# print(mf)

# import pandas as pd

# mf = pd.read_csv("students.csv")

# print(mf)

# for index, row in df.iterrows():
#     print(row["Name"])

import pandas as pd

df=pd.read_csv("students.csv")

for index, row in df.iterrows():
    print(row["Name"],row["Marks"])

# import pandas as pd

# df = pd.read_csv("students.csv")

# df.columns = df.columns.str.strip()

# for index, row in df.iterrows():
#     print(row["Name"], row["Marks"])