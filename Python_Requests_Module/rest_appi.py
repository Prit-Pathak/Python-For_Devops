from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to num check page"


@app.route("/api/check_even/<int:num>")
def check_even(num):
    res = {
        "number": num,
        "is_even": num % 2 == 0,
    }
    return res


if __name__ == "__main__":
    app.run(debug=True)
