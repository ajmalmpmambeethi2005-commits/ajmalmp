students = [
    {"math": 80, "science": 70},
    {"math": 90, "science": 80}
]


for student in students:

    average = (
        student["math"] + student["science"]
    ) / 2

    print(average)