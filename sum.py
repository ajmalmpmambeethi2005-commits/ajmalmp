from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Ajmal's Student Portal!"

@app.route("/about")
def about():
    return "This is a student portal built using Flask."

@app.route("/student")
def student():
    return "Student Name: Ajmal | Course: Data Science"

if __name__ == "__main__":
    app.run(debug=True)