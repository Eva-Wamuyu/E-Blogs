from Blog.app import db,bcrypt
from werkzeug.security import generate_password_hash,check_password_hash

class Writer(db.Model):

  

  _id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  user_name = db.Column(db.String,unique=True)
  email = db.Column(db.String,unique=True)
  passwd = db.Column(db.String)
  posts = db.Column(db.String) 
  profilePath = db.Column(db.String)

  def __init__(self,name,user_name,email,passwd,profilePath):
    self.name = name
    self.user_name = user_name
    self.email = email
    self.passwd = generate_password_hash(passwd)
    #self.passwd = bcrypt.generate_password_hash(passwd).decode('utf8')
    self.profilePath = profilePath


  #def authenticate(self,passKey):
    #return bcrypt.check_password_hash ( bcrypt.generate_password_hash(passKey).decode('utf8'), self.passwd)

  def authenticate(self,passed):
    return check_password_hash(self.passwd,passed)

  def __repr__(self):
    return f'name: {self.name}, user_name: {self.user_name},email: {self.email}'

    
  
  

  


  

