from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms.fields import PasswordField, SubmitField, StringField
from wtforms.validators import Email, Length, DataRequired


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[
        Email()
    ])
    password = PasswordField("Senha", validators=[
        Length(3, 6, "O campo deve conter de 3 a 6 caracteres")
    ])
    submit = SubmitField("Logar")



class RegisterForm(FlaskForm):
    name = StringField("Nome", validators=[
        DataRequired("O campo é obrigatório")
    ])
    email = EmailField("Email", validators=[
        Email()
    ])
    password = PasswordField("Senha", validators=[
        Length(3, 6, "O campo deve conter de 3 a 6 caracteres")
    ])
    submit = SubmitField("Registrar")