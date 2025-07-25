from flask import Flask,render_template,redirect,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")
        
        return render_template("thankyou.html", name=name, message=message)
    return render_template("contact.html")

@app.route("/about")
def about():

    return render_template("about.html")