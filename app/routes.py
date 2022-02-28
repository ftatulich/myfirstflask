# -*- coding: utf-8 -*-
from app import app
from flask import render_template
from forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Jack"}
    return render_template("index.html", title="Home", user=user)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Sign in", form=form)
