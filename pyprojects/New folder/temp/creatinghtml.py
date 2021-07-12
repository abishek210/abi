from flask import Flask, render_template

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/")
def home():
    return render_template("index.html", content="Testing")

    @app.route("/")
def home():
    return render_template("index.html", content={"a":2, "b":"hello"})