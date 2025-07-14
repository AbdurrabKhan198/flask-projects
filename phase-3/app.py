from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")

        return render_template("thankyou.html", name=name, message=message)

    return render_template("feedback.html")