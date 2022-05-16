from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField,PasswordField
from wtforms.validators import DataRequired,EqualTo, Email




class BlogForm(FlaskForm):
   post = TextAreaField("Blog Here")
   title = StringField("Title", validators=[DataRequired()])
   brief = StringField("Brief", validators=[DataRequired()])
   category = SelectField("Category",choices=[("Gadgets","Gadgets"),("Data Structures","Data Structures"), ("Algorithms","Algorithms")] ,validators=[DataRequired()])
   img = StringField("Path")
   #img_path = FileInput("Image")
   submit = SubmitField("Post")


class CommentForm(FlaskForm):
  author = StringField("Your Name",validators=[DataRequired()])
  comment = TextAreaField("Your comment",validators=[DataRequired()])
  submit = SubmitField("Comment")



class RegForm(FlaskForm):
  email = StringField("Email Address", validators=[DataRequired(), Email()])
  name = StringField("Your Name", validators=[DataRequired()])
  username = StringField("Username", validators=[DataRequired()])
  password = PasswordField("Password", validators=[DataRequired(), EqualTo('passwordtwo')])
  passwordtwo = PasswordField("Password Two")
  submit = SubmitField("Sign Up")
  



class LoginForm(FlaskForm):
  email = StringField("Email", validators=[DataRequired(), Email()])
  password = PasswordField("Password", validators=[DataRequired()])
  submit = SubmitField("Login")

