from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")

def student():
    return render_template(
        "profile.html",
        name = "abdurrab",
        is_topper = True,
        subjects = ["Maths","Science","History"]

    )