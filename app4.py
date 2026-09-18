from flask import Flask,render_template

app=Flask(__name__)
@app.route("/")
def home():
    students = ["Ajmal", "Rahul", "Anu", "Sara"]
    return render_template("app4.html", students=students)

__name__=="__main__"
app.run(debug="True")