



from flask import Flask,render_template,request,redirect
from firewall import add_rule,get_rules
import sqlite3

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def login():
    if request.method=="POST":
        if request.form["username"]=="admin" and request.form["password"]=="admin":
            return redirect("/dashboard")
    return render_template("login.html")

@app.route("/dashboard",methods=["GET","POST"])
def dashboard():

    if request.method=="POST":
        ip=request.form["ip"]
        port=request.form["port"]
        action=request.form["action"]
        add_rule(ip,port,action)

    rules=get_rules()

    blocked=len([r for r in rules if r[3]=="BLOCK"])
    allowed=len([r for r in rules if r[3]=="ALLOW"])

    return render_template(
        "dashboard.html",
        rules=rules,
        blocked=blocked,
        allowed=allowed
    )


if __name__=="__main__":
    app.run(debug=True)
