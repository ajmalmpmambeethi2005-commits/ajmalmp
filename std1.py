from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)


def process_csv(file):

    df = pd.read_csv(file)

    if df.empty:
        return "The file is empty"

    required_columns = ["name", "age", "course"]

    for i in required_columns:
        if i not in df.columns:
            return f"Missing column: {i}"

    df["age"] = pd.to_numeric(df["age"], errors="coerce")

    if df["age"].isna().any():
        return "Age contains non-numeric values"

    average = df["age"].mean()

    return f"Average age: {average}"


# ADD THIS
@app.route("/")
def home():
    return render_template("std1.html")


@app.route("/upload", methods=["POST"])
def upload():

    if "file" not in request.files:
        return "No file uploaded"

    file = request.files["file"]

    if file.filename == "":
        return "No file selected"

    result = process_csv(file)

    return result


if __name__ == "__main__":
    app.run(debug=True)