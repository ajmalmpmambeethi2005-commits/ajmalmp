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

    df["Total"] = df["Math"] + df["Science"] + df["English"]

    df["Average"] = df["Total"] / 3

    df["Average"] = df["Average"].round(2)

    df["Grade"] = df["Average"].apply(get_grade)

    df["Result"] = df["Average"].apply(
        lambda x: "Pass" if x >= 40 else "Fail"
    )

    return df


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["file"]

    df = process_csv(file)

    class_average = df["Average"].mean()

    top_index = df["Average"].idxmax()

    top_student = df.loc[top_index, "Name"]

    passed = (df["Result"] == "Pass").sum()

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