from flask import Flask,request,Response,redirect,session,url_for,render_template

app = Flask(__name__)
app.secret_key = "supersecret"

@app.route("/", methods=["POST","GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password =="123":
            session["user"] = username
            return redirect(url_for("welcome"))

            
        else:
            return Response("invalid credentials - try again", mimetype="text/plain")
    else:
        return render_template("home.html")
    
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
        <h1>welcome {session["user"]}</h1>
        <a href={url_for('logout')}> logout</a>
        '''
    else:
        return redirect(url_for("login"))
    
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))