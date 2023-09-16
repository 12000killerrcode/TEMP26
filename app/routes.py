from app import app
from flask import Flask
from flask import render_template


@app.route('/')
@app.route('/Index')
def index():
    """Index URL"""
    return render_template('index.html', title='Index Page')

@app.route('/Register')
def register():
    """Register URL"""
    return render_template('register.html', title='Register Page')

@app.route('/shop')
def shop():
    """Shop URL"""
    return render_template('shop.html', title='Shop Page')

@app.route('/Login')
def login():
    """Login URL"""
    return render_template('login.html', title='Login Page')
    

