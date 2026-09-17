from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("hallo1.html")

@app.route("/health")
def health():
    return render_template("result.html")