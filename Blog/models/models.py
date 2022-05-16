from Blog.app import db


class Comment(db.Model):
  __tablename__ = 'comments'

  _id = db.Column(db.Integer, primary_key=True)
  commentor = db.Column(db.String(255), nullable=False)
  date = db.Column(db.Date)
  postId = db.Column(db.Integer, db.ForeignKey('blogs._id'))
  body = db.Column(db.String(255), nullable=False)
  def __init__(self,commentor,body,date,postId):
    self.commentor = commentor
    self.date = date
    self.body = body
    self.postId = postId

  def __repr__(self):
    return f"id = {self._id}, commentor = {self.commentor}, date: {self.commentor},date: {self.date},postId: {self.postId}"

  def store(self,field):
    db.session.add(field)
    db.session.commit()
    
  @classmethod
  def remove(cls,sth):
    db.session.delete(sth)
    db.session.commit()
  
  



class Blog(db.Model):

  __tablename__ = 'blogs'
  _id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.Text, nullable=False)
  body = db.Column(db.Text, nullable=False)
  date = db.Column(db.Date)
  category = db.Column(db.Text, nullable=False)
  img_path = db.Column(db.Text)
  brief = db.Column(db.Text)
  comments = db.relationship('Comment',backref='blogs',lazy='dynamic')
  authorId = db.Column(db.Integer, db.ForeignKey('writer._id'))

  def __init__(self,title,body,date,category,img_path,brief,authorId):
    self.title = title
    self.body = body
    self.date = date
    self.category = category
    self.img_path = img_path
    self.brief = brief
    self.authorId = authorId

  def __repr__(self):
    return f'id: {self._id}, title: {self.title}, body: {self.body}, date:{self.date}, category:{self.category}, img_path:{self.img_path}'


  @classmethod
  def remove(cls,sth):
    db.session.delete(sth)
    db.session.commit()

  
  def store(self,field):
    db.session.add(field)
    db.session.commit()

  def fetchComments(self,id):
    comments = Comment.query.filter_by(postId=id).all()
    return comments

  def getLast(self, sth):
    post = Blog.query.all()
    maxi = max(post)
    return Blog.query.filter_by(_id=maxi)


    
    
