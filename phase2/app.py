from flask import Flask,request,Response,redirect,session,url_for,render_template

app = Flask(__name__)
# app.secret_key = "supersecret"

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/submit", methods=["GET","POST"])
def welcome():
    username = request.form.get("username")
    password = request.form.get("password")

    # if username == "admin" and password == "123":
    #     # session['user'] = username
        
    #     return render_template("welcome.html", name = username)
    valid_crediantial = {
        'admin' : '123',
        'abdurrab' : '23'
    }
    if username in valid_crediantial and password == valid_crediantial[username]:
        return render_template("welcome.html", name=username)

    else:
        return render_template("login.html")