from flask import Flask, render_template,request,url_for, redirect,flash

from forms import RegistrationForm

app = Flask(__name__)
app.secret_key = "mysecretkey"

# @app.route("/feedback", methods=["GET", "POST"])
# def feedback():
#     if request.method == "POST":
#         name = request.form.get("name")
#         message = request.form.get("message")

#         return render_template("thankyou.html", name=name, message=message)

#     return render_template("feedback.html")

# @app.route("/", methods=["GET", "POST"])
# def form():
#     if request.method == "POST":
#         name = request.form.get("name")
#         message = request.form.get("message")
#         if not name:
#             flash("Name can not be empty", "error")
#             return redirect(url_for("form"))
#         flash(f"THanks {name} for your feedback {message}" , "success")
#         return redirect(url_for("thankyou"))

#     return render_template("form.html")

# @app.route("/thankyou",methods=["GET"])
# def thankyou():
#         message = request.args.get("message")
#         return render_template("thankyou.html",message=message)
        

@app.route("/", methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        flash(f"Welcome , {name}! Your registered sucessfully","success")
        return redirect(url_for("success"))
    return render_template("register.html", form=form)

@app.route("/success")
def success():
    return render_template("success.html")