from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    student = "Ajmal"
    age = 20

    return render_template(
        "home.html",
        student=student,
        age=age
    )

if __name__ == "__main__":
    app.run(debug=True)