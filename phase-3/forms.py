from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import DataRequired,Email, Length

class RegistrationForm(FlaskForm):
    name = StringField("Full name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(),Email()])
    password = StringField("Password", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Register")