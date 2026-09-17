from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("hallo.html")


@app.route("/student", methods=["POST"])
def student():

    # Get form data
    name = request.form.get("name", "").strip()
    age = request.form.get("age", "").strip()
    mark = request.form.get("mark", "").strip()
    phone = request.form.get("phone", "").strip()
    email = request.form.get("email", "").strip()


    # Name validation
    if not name:
        return "Name is required"


    # Age validation
    if not age:
        return "Age is required"

    try:
        age = int(age)
    except ValueError:
        return "Age must be a number"

    if age < 1 or age > 120:
        return "Invalid age"


    # Mark validation
    if not mark:
        return "Mark is required"

    try:
        mark = float(mark)
    except ValueError:
        return "Mark must be a number"

    if mark < 0 or mark > 100:
        return "Mark must be between 0 and 100"


    # Phone validation
    if not phone:
        return "Phone number is required"

    if not phone.isdigit():
        return "Phone number must contain only numbers"

    if len(phone) != 10:
        return "Phone number must contain 10 digits"


    # Email validation
    if not email:
        return "Email is required"

    if "@" not in email or "." not in email:
        return "Invalid email address"


    return f"""
    Name: {name}<br>
    Age: {age}<br>
    Mark: {mark}<br>
    Phone: {phone}<br>
    Email: {email}
    """


if __name__ == "__main__":
    app.run(debug=True)