from . import user
from flask_login import login_required
from flask import render_template
from app.models import User


@user.route("/")
def index():
    users = User.query.all()
    return render_template("index.html", users=users)



@user.route('/user/<int:id>')
@login_required
def unique(id):
    user = User.query.get(id)
    return render_template("user.html", user=user)