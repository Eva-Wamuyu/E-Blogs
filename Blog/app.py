import os
from flask import Flask, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_simplemde import SimpleMDE

app = Flask(__name__,instance_relative_config=True)

from .user.userviews import userview
from .writer.writerviews import writer_view
app.register_blueprint(userview)
app.register_blueprint(writer_view, url_prefix="/EAdmin")

basedirectory =os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+os.path.join(basedirectory,'database.sqlite')
app.config['SIMPLEMDE_JS_IIFE'] = True
app.config['SIMPLEMDE_USE_CDN'] = True
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
mde = SimpleMDE(app)

app.config['SECRET_KEY'] = "hehe public"



@app.route("/")
def base():
  return redirect(url_for('userview.index'))

def create_app():
    app.run(debug=True)




