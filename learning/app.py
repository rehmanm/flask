from flask import Flask, render_template, session, redirect, flash, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

from NameForm import NameForm

app = Flask(__name__)
moment = Moment(app)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'hard to guess string'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()

    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash("You have changed your name")
            
        session['name'] = form.name.data
        return redirect(url_for('index'))   

    return render_template("index.html", current_time = datetime.utcnow(), form=form, name = session.get('name'))

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('name', None)
   return redirect(url_for('index'))

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500
