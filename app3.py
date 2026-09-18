from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def home():
    age=15
    return render_template("app3.html" ,age=age)

__name__=="__main__"
app.run(debug="True")