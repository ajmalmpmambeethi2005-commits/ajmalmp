from flask import Flask,render_template,request

app=Flask(__name__)
@app.route("/")
def home():
    return render_template("app11.py")

@app.route("/submit" ,methods=["POST"])
def submit():

    name=request.form.get("name","").strip()
    email=request.form.get("email","").strip()
    number=request.form.get("number","").strip()

    if not name:
        return "name is requred"
    if not name.replace(" ","").isalpha():
        return "name contain only letters"

    