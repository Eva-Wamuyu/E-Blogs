from ..user import userview
from flask import render_template


@userview.app_errorhandler(404)
def notFound(e):
  return render_template('usertemps/notfound.html'),404