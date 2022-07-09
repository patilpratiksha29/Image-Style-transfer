from flask import Flask, render_template, request,session,redirect,flash,url_for,send_from_directory, redirect, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from datetime import datetime
import json
import os
import pandas as pd
import test
import neuralStyleProcess
import cv2
from flask_mysqldb import MySQL
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import re

import numpy as np


with open('config.json', 'r') as c:
    params = json.load(c)["params"]


APP_ROOT = os.path.dirname(os.path.abspath(__file__))

local_server = True
app = Flask(__name__,template_folder='templates')
app.secret_key = 'super-secret-key'

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = params['gmail_user']
app.config['MAIL_PASSWORD'] = params['gmail_password']
mail = Mail(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'image'

mysql = MySQL(app)

if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)

class Register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    uname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(10), nullable=False)
    cpassword = db.Column(db.String(10), nullable=False)

class Contact(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    email=db.Column(db.String(50),nullable=False)
    subject=db.Column(db.String(50),nullable=False)
    message=db.Column(db.String(250),nullable=False)

@app.route("/")
def Home():
    return render_template('index.html',params=params)

@app.route("/about")
def About():
    return render_template('about.html',params=params)

@app.route("/album")
def Album():
    return render_template('album.html',params=params)

@app.route("/register", methods=['GET','POST'])
def register():
    if(request.method=='POST'):
        name = request.form.get('name')
        uname = request.form.get('uname')
        email= request.form.get('email')
        password= request.form.get('password')
        cpassword= request.form.get('cpassword')

        user=Register.query.filter_by(email=email).first()
        if user:
            flash('Account already exist!Please login','success')
            return redirect(url_for('register'))
        if not(len(name)) >3:
            flash('length of name is invalid','error')
            return redirect(url_for('register')) 
        if (len(password))<8:
            flash('length of password should be greater than 7','error')
            return redirect(url_for('register'))
        else:
             flash('You have registered succesfully','success')
            
        entry = Register(name=name,uname=uname,email=email,password=password,cpassword=cpassword)
        db.session.add(entry)
        db.session.commit()
    return render_template('register.html',params=params)


@app.route('/login', methods =['GET', 'POST'])
def login():
	msg = ''
	if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
		email = request.form['email']
		password = request.form['password']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM register WHERE email = % s AND password = % s', (email, password, ))
		account = cursor.fetchone()
		if account:
			session['loggedin'] = True
			session['id'] = account['id']
			session['email'] = account['email']
			msg = 'Logged in successfully !'
			return render_template('dashboard.html', msg = msg)
		else:
			msg = 'Incorrect username / password !'
	return render_template('login.html', msg = msg)

@app.route("/dashboard")
def display():
	if 'loggedin' in session:
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM register WHERE id = % s', (session['id'], ))
		account = cursor.fetchone()	
		return render_template("dashboard.html",account = account)
	return redirect(url_for('login'))
	

@app.route("/contact",  methods=['GET','POST'])
def contact():
    if(request.method =='POST'):
        name=request.form.get('name')
        email=request.form.get('email')
        subject=request.form.get('subject')
        message=request.form.get('message')
        entry=Contact(name=name,email=email,subject=subject,message=message)
        db.session.add(entry)
        db.session.commit()
    return render_template('contact.html',params=params)


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", params=params)

@app.route('/result')
def video():
    import webcam_app
    return render_template('/result.html')

@app.route("/dashboard", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print("TARGET", target)

    if not os.path.isdir(target):
        os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))

    data = request.form.get("style")
    print(data)

    myFiles = []

    for file in request.files.getlist("file"):
        print("file", file)
        filename = file.filename
        print("filename", filename)
        destination = "".join([target, filename])
        print("destination", destination)
        file.save(destination)
        myFiles.append(filename)
    print(myFiles)

    return render_template("result.html", image_names=myFiles, selected_style=data)

# in this function send_image will HAVE to take in the parameter name <filename>
@app.route('/dashboard/<filename>')
def send_original_image(filename):
    return send_from_directory("images", filename)

@app.route('/result/<filename>/<selected_style>')
def send_processed_image(filename, selected_style):
    directoryName = os.path.join(APP_ROOT, 'images/')

    newImg = neuralStyleProcess.neuralStyleTransfer(directoryName, filename, selected_style)
    
    return send_from_directory("images", newImg)


@app.route("/logout", methods = ['GET','POST'])
def logout():
    session.pop('email')
    return redirect(url_for('Home')) 



if __name__ == '__main__':
    app.run(debug=True)