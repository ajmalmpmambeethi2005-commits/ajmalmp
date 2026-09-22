from flask import Flask,jsonify

app=Flask(__name__)

@app.route("/student")
def student():
    return jsonify({
        "name": "Ajmal",
        "age": 21,
        "marks": 85
    })