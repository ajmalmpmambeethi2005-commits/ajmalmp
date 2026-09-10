from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Ajmal's Store!"

@app.route("/product")
def product():
    return "Product: Laptop"

@app.route("/price")
def price():
    return "Price: ₹50,000"

@app.route("/contact")
def contact():
    return "Contact us at: 9876543210"

if __name__ == "__main__":
    app.run(debug=True)