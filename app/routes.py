from flask_login import login_required, login_user, logout_user
from flask import render_template, redirect, url_for
from app.models import User
from app.forms import LoginForm, RegisterForm
from werkzeug.security import check_password_hash, generate_password_hash
from app import db



def init_app(app):
    @app.route("/login", methods=["GET", "POST"])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            user = User.query.filter_by(email=email).first()
            if not user:
                return redirect(url_for(".login"))
            if not check_password_hash(user.password, password):
                return redirect(url_for(".login"))
            login_user(user)
            return "Logado"
        return render_template("login.html", form=form)




    @app.route('/register', methods=["GET", "POST"])
    def register():
        form = RegisterForm()
        if form.validate_on_submit():
            user = User()
            user.name = form.name.data
            user.email = form.email.data
            user.password = generate_password_hash(form.password.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("index"))

        return render_template("register.html", form=form)



    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for("index"))
    
    
    @app.route("/")
    def index():
        users = User.query.all()
        return render_template("index.html", users=users)



    @app.route('/user/<int:id>')
    @login_required
    def user(id):
        user = User.query.get(id)
        return render_template("user.html", user=user)