from flask import Blueprint

userview = Blueprint("userview",__name__,static_folder="./../static",template_folder="Blog/templates")

from . import userviews,errors