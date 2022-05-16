from flask import render_template, redirect, url_for, flash, Blueprint
import datetime
from .forms import CommentForm
from ..apireq import getRandomQuote
from . import userview
#from models import Blog






@userview.route('/')
def index():
  from ..models.models import Blog

  quote = getRandomQuote()
  
  blogs = Blog.query.all()

  return render_template('usertemps/index.html',quote=quote,blogs=blogs)


@userview.route('/post/<post>',methods=['POST', 'GET'])
def post(post):
  from ..models.models import Blog
  blog = Blog.query.filter_by(_id=post).first()

  return render_template('usertemps/post.html',blog=blog)

@userview.route("/comment/<post>", methods=["GET","POST"])
def comment(post):
   from ..models.models import Comment
   form = CommentForm()
   
   print(form)
   if form.validate_on_submit():
    comment = Comment(commentor=form.author.data,date=datetime.date.today(),postId=post,body=form.comment.data)
    comment.store(comment)
    flash("Your comment has been recorded")
    return redirect(url_for('userview.post',post=post))
   print(form.validate())
   return render_template('usertemps/comment.html',form=form)


@userview.route('/about/writer')
def aboutWriter():
  from ..models.writer import Writer
  writer = Writer.query.filter_by(_id=1).first()

  return render_template('usertemps/profile.html',writer=writer)

@userview.route('/latest')
def latest():
  from ..models.models import Blog
  post = Blog.query.first()

  return render_template('usertemps/post.html',blog=post)



