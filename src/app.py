from flask import Flask, render_template, request, redirect, url_for, flash
from config import config

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        user = request.form['username']
        password = request.form['password']
        return render_template("auth/entro.html")
    else:
        return render_template('auth/login.html')


@app.route("/entro")
def escritorio():
    return render_template("auth/entro.html")


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()
