from flask import Flask, request,redirect,url_for,session,Response

# this is the main application file for the Flask app, it tells
app = Flask(__name__) 
app.secret_key = "supresecret"


#home page/login page
@app.route("/", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == "admin" and password == "123":
            session["user"] = username #store in session

            return redirect(url_for("welcome"))
        else:
            return Response("invalid credential", mimetype="text/plain")
    else:
        return '''
        <h1>login page</h1>
        <form method="POST" >
        username : <input type="text" name="username" > </br>
        password : <input type="text" name = "password" > </br>
        <input type="submit" value = "login">
                
        '''
#welcome page after login
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f''' 
        <h1>welcome {session["user"]}</h1>
        <a href={url_for('logout')}> logout</a>
        
        '''
    else:
        return redirect(url_for("login"))
    
#logout page
@app.route("/logout")
def logout():
    session.pop("user", None)

    return redirect(url_for("login"))