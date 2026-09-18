from flask import Flask,jsonify

app=Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "name":"ajmal",
        "age":21,
        "course":"stati"

    })

@app.route("/health")
def health():
    return jsonify({
        "name":"amal",
        "age":21,
        "course":"maths"

    })

if __name__=="__main__":
    app.run(debug=True)