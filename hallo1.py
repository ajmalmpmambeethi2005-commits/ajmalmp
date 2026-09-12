from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["myfile"]

    return "You uploaded: " + file.filename

if __name__ == "__main__":
    app.run(debug=True)