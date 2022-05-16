from flask import Blueprint, render_template, redirect, session, url_for
from .forms import RegForm, LoginForm, BlogForm
import jwt
import datetime


writer_view = Blueprint('writer_view',__name__,static_folder="./../static",template_folder="./../templates")

key = "public key"

@writer_view.route('/',methods=["POST","GET"])
def writerIndex():
  form1 = LoginForm()
  
  if form1.validate_on_submit():
    from ..models.writer import Writer
    person = Writer.query.filter_by(email=form1.email.data).first()
    if person is not None:
      #person.authenticate("22222","22222")
      #print(person.authenticate(form1.password.data, person.passwd))
      if person.authenticate(form1.password.data):
        print("inn")
      #if form1.password.data == person.passwd:
        user = {'email': form1.email.data}
        
        time = int(datetime.datetime.now().timestamp())+100
        jwt_token = jwt.encode({'user':user,'exp':time},key="hehe publik",algorithm="HS256")
        session['jwt'] = jwt_token
        print(jwt_token)
        return redirect(url_for('.main'))
  return render_template('writertemps/login.html',form1=form1)

@writer_view.route('/post',methods=['POST','GET'])
def main():
  form = BlogForm()
  if confirmToken():
    
    if form.validate_on_submit():
      from ..models.models import Blog
      blog = Blog(title = form.title.data, body=form.post.data,date= datetime.datetime.now(),category =form.category.data,img_path = form.img.data, brief=form.brief.data,authorId=1)
      blog.store(blog)
      print(confirmToken())
      return redirect(url_for('.posts'))
  print(form.validate_on_submit())
  return render_template('writertemps/index.html',form=form)

@writer_view.route('/allposts')
def posts():
  from ..models.models import Blog  
  blogs = Blog.query.all()
  if confirmToken():
    
    return render_template('writertemps/posts.html',posts=blogs)
  #return render_template('writertemps/posts.html',posts=blogs)
  return redirect(url_for('.writerIndex'))


@writer_view.route('/delp/<post>')
def del_success(post):
  if confirmToken():
    from ..models.models import Blog
    post = Blog.query.filter_by(_id =post).first()
    Blog.remove(post)
    return render_template('writertemps/success.html')
  return redirect(url_for('.writerIndex'))

@writer_view.route('/delc/<post>')
def del_comment(post):
  if confirmToken():
      from ..models.models import Comment
      comment = Comment.query.filter_by(_id=post).first()
      Comment.remove(comment)
      return render_template('writertemps/success.html')
  return redirect(url_for('.writerIndex'))


@writer_view.route("/editprofile")
def profile():
  return render_template('writertemps/profile.html')

@writer_view.route('/edit/<post>',methods=['POST','GET'])
def edit(post):
  from ..models.models import Blog
  specblog = Blog.query.filter_by(_id = post).first()
  form = BlogForm()
  print(specblog)
  print(form.validate_on_submit()) 
  if form.validate_on_submit():
    return redirect(url_for('.main'))
  return render_template('writertemps/edit.html', form=form)


def confirmToken():
  if 'jwt' in session:
    token = session['jwt']
    try:
      user = jwt.decode(token,key="hehe publik",algorithms="HS256")
    except Exception as e:
      return redirect(url_for('.writerIndex'))
    else:
      return user
  return False

