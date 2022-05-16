from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

SECRET_KEY = 'hehe public key'

class CommentForm(FlaskForm):
  author = StringField("Your Name",validators=[DataRequired()])
  comment = TextAreaField("Your comment",validators=[DataRequired()])
  submit = SubmitField("Comment")

  