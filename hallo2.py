from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("upload1.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]

    content = file.read().decode("utf-8")

    return content.replace("\n","<br>")

if __name__ == "__main__":
    app.run(debug=True)