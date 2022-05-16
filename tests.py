import unittest
from Blog.models.models import Blog, Comment
from Blog.models.writer import Writer
import datetime
from werkzeug.security import check_password_hash,generate_password_hash
from Blog.apireq import Quote


class TestBlog(unittest.TestCase):
  '''
  Testing the blog model
  '''

  def setUp(self):
    '''
    Setup method
    '''
    self.blog = Blog("title","body",datetime.datetime.today,"category","path","brief",2)

  def test_initializer(self):
    '''
     Test intitialization
    '''
    self.assertEqual(self.blog.title,"title")
    self.assertEqual(self.blog.body,"body")
    self.assertEqual(self.blog.date,datetime.datetime.today)
    self.assertEqual(self.blog.category,"category")
    self.assertEqual(self.blog.img_path,"path")
    self.assertEqual(self.blog.brief,"brief")
    self.assertEqual(self.blog.authorId,2)

  

class TestComment(unittest.TestCase):
  def setUp(self):
    self.comment = Comment("wamuyu","booody",datetime.datetime.today,1)

  def testInit(self):
    self.assertEqual(self.comment.commentor, "wamuyu")
    self.assertEqual(self.comment.body,"booody")
    self.assertEqual(self.comment.date,datetime.datetime.today)
    self.assertEqual(self.comment.postId,1)


class TestWriter(unittest.TestCase):

  def setUp(self):
    self.newWriter = Writer("wamuyu","wamuyu","eva@gmail.com","nicki","none")

  def testInitializer(self):
    self.assertEqual(self.newWriter.name,"wamuyu")
    self.assertEqual(self.newWriter.user_name,"wamuyu")
    self.assertEqual(self.newWriter.email,"eva@gmail.com")
    check_password_hash(self.newWriter.passwd,generate_password_hash("nicki"))
    self.assertEqual(self.newWriter.profilePath,"none")


class TestQuote(unittest.TestCase):
  def setUp(self):
    self.quote = Quote("ada","best quote")

  def testInit(self):
    self.assertEqual(self.quote.author,"ada")
    self.assertEqual(self.quote.quote,"best quote")
    

  



if __name__ == "__main__":
  unittest.main()