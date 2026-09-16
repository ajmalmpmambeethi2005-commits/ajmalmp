# from flask import Flask,render_template,request
# import pandas as pd

# app=Flask(__name__)

# def get_grade(avg)
#     if avg>=90:
#         return "A"
#     elif avg>=80:
#         return "B"
#     elif avg>=70:
#         return "C"
#     elif avg>=60:
#         return "D"
#     else:
#         return "F"

# def process_csv(file):

#     df = pd.read_csv(file)

#     df["Total"]=df["data science"]+ df["practical"]+ df["gk"]

#     df["Average"]=df["Total"]/3



#     df["grade"]=df["Average"].apply("get_grade")

#     df["Result"]=df["Average"].apply(lambda x:"pass" if x>= 60 else "fail")

#     class_Average=df["Average"].mean()

#     return df

# @app.route("/")
# def home():
#     return render_template("hallo.html")

# @app.route("/upload", methods=["POST"])
# def upload():
#     file=request.file["file"]
#     df=pd.read_csv(file)
#     # render_template("result.html")


#     highest_index=df["Average"].idxmax()
#     top_student=df.loc[highest_index,"name"]
#     passed=(df["Result"]=="pass").sum()
#     Total_students=len(df)
#     pass_percentage=(passed/Total_students)*100


#     return render_template(
#         "result.html",
#         tables=[df.to_html(classes="table")],
#         class_average=round(class_average,2),
#         top_student=top_student,
#         pass_percentage=round(pass_percentage,2)
# )



# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)


def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def process_csv(file):

    df = pd.read_csv(file)

    df["Total"] = (
        df["data science"]
        + df["practical"]
        + df["gk"]
    )

    df["Average"] = df["Total"] / 3

    df["grade"] = df["Average"].apply(get_grade)

    df["Result"] = df["Average"].apply(
        lambda x: "pass" if x >= 60 else "fail"
    )

    return df


@app.route("/")
def home():
    return render_template("hallo.html")


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["file"]

    df = process_csv(file)

    class_average = df["Average"].mean()

    highest_index = df["Average"].idxmax()

    top_student = df.loc[highest_index, "name"]

    passed = (df["Result"] == "pass").sum()

    total_students = len(df)

    pass_percentage = (passed / total_students) * 100

    return render_template(
        "result.html",
        tables=[df.to_html(classes="table")],
        class_average=round(class_average, 2),
        top_student=top_student,
        pass_percentage=round(pass_percentage, 2)
    )


if __name__ == "__main__":
    app.run(debug=True)