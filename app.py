from flask import Flask,request,render_template
import mysql.connector
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/login",methods=["POST"])
def login():
    msg=''
    username=request.form["username"]
    password=request.form["password"]
    mydb=mysql.connector.connect(
    host="remotemysql.com",
    user="Rz8hqnldk4",
    password="nd0wK03xe0",
    database="Rz8hqnldk4"
    )
    mycursor=mydb.cursor()
    mycursor.execute( "SELECT * FROM LoginDetails WHERE Name = %s AND Password = %s", (username, password) )
    account = mycursor.fetchone()
    if account:
     print('login success')
     name = account[1]
     id = account[0]
     msg = 'Logged in Successfully'
     print('login successful!')
    else:
     msg = 'incorrect Credentials. Kindly check'
     return render_template('login.html', msg=msg,name=name,id=id)
