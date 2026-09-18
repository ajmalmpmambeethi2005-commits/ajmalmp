from flask import Flask,render_template,request

app=Flask(__name__)
@app.route("/home", methods=["GET"])
def home():
    return render_template("app5.html")

@app.route("/register",methods=["POST"])
def register():
    name=request.form["name"]
    return f"hai {name}, health is okey"

__name__="__main__"
app.run(debug="True")


# from flask import Flask, render_template, request

# app = Flask(__name__)


# @app.route("/home", methods=["GET"])
# def home():
#     return render_template("app5.html")


# @app.route("/register", methods=["POST"])
# def register():
#     name = request.form["name"]
#     return f"Hello {name}, registration successful!"


# if __name__ == "__main__":
#     app.run(debug=True)