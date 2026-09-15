# # from flask import Flask, request, jsonify

# # app = Flask(__name__)


# # @app.route("/api/health", methods=["GET"])
# # def health():
# #     return jsonify({
# #         "status": "working"
# #     })


# # @app.route("/api/analyze", methods=["POST"])
# # def analyze():

# #     data = {
# #         "students": [
# #             {
# #                 "math": 80,
# #                 "science": 75,
# #                 "english": 90
# #             }
# #         ]
# #     }

# #     students = data["students"]

# #     averages = []
# #     passed = 0

# #     for student in students:

# #         average = (
# #             student["math"]
# #             + student["science"]
# #             + student["english"]
# #         ) / 3

# #         averages.append(average)

# #         if average >= 40:
# #             passed += 1

# #     class_average = sum(averages) / len(averages)

# #     top_average = max(averages)

# #     pass_percentage = (passed / len(students)) * 100

# #     return jsonify({
# #         "students": students,
# #         "class_average": round(class_average, 1),
# #         "top_average": round(top_average, 1),
# #         "pass_percentage": round(pass_percentage, 1)
# #     })


# # if __name__ == "__main__":
# #     app.run(debug=True)


from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/analyze", methods=["POST"])
def analyze():

    data = request.json

    students = data["students"]

    averages = []
    passed = 0

    for student in students:

        average = (
            student["math"]
            + student["science"]
            + student["english"]
        ) / 3

        averages.append(average)

        if average >= 40:
            passed += 1

    class_average = sum(averages) / len(averages)

    top_average = max(averages)

    pass_percentage = (passed / len(students)) * 100

    return jsonify({
        "students": students,
        "class_average": round(class_average, 1),
        "top_average": round(top_average, 1),
        "pass_percentage": round(pass_percentage, 1)
    })


if __name__ == "__main__":
    app.run(debug=True)



# students = [
#     {"math": 80, "science": 70},
#     {"math": 90, "science": 80}
# ]


# for student in students:

#     average = (
#         student["math"] + student["science"]
#     ) / 2

#     print(average)