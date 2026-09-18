# import pandas as pd

# data={
#     "name":["ajmal","ashmal","sinan"],
#     "age":[21,22,23],
#     "mark":[90,32,34]

# }
# df=pd.DataFrame(data)
# print(df)




# import pandas as pd

# data={
#     "name":["ajmal","amal","lalu"],
#     "age":[12,21,23],
#     "mark":[12,23,34]
# }

# df=pd.DataFrame(data)
# print(df["mark"])



# import pandas as pd

# data={
#     "name":["ajmal","amal","ashmal"],
#     "age":[12,21,23],
#     "mark":[23,32,45]
# }

# df=pd.DataFrame(data)
# # average=df ["mark"].mean()
# # passed=df[df["mark"]>=30]
# # result= df["Mark"].apply(
# #     lambda mark: "Pass" if mark >= 80 else "Fail"
# # )


# print(df)

# topstudent = df.loc[df["Mark"].idxmax()]

# # print("average mark is:", average)
# # print("pass student:", passed)
# print("top_student:")
# print(topstudent)


import pandas as pd

data = {
    "Name": ["Ajmal", "Rahul", "Anu"],
    "Age": [20, 21, 19],
    "Mark": [85, 75, 92]
}

df = pd.DataFrame(data)

print(df)

topstudent = df.loc[df["Mark"].idxmax()]

print("Top Student:")
print(topstudent)