from flask import Flask, render_template
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
    name = None
    form = NameForm()

    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''

    return render_template("index.html", current_time = datetime.utcnow(), form=form, name = name)

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500
