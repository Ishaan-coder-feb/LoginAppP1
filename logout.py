from flask import Flask,render_template
app=Flask(__name__)
@app.route("/logout")
def logout():
    name=''
    id=''
    msg="Logged Out Successfully"
    return render_template("index.html",name=name,id=id,msg=msg)

