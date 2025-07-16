from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import DataRequired,Email, Length

class RegistrationForm(FlaskForm):
    name = StringField("Full name", validators=[DataRequired(message="Name is required")])
    email = StringField("Email", validators=[DataRequired(message="email message is required"),Email("That does not look like a valid email")])
    password = StringField("Password", validators=[DataRequired(message="password is required"), Length(min=6, message="Password must be at least 6 characters long")])
    submit = SubmitField("Register")