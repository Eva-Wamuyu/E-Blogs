import unittest
from ..Blog.models.models import *


class TestBlog(unittest.TestCase):
  '''
  Testing the blog model
  '''

  def setUp(self):
    '''
    Setup method
    '''
    self.blog = Blog("title","body","date","categpry","path","brief",2)

  def initializer(self):
    '''
     Test intitialization
    '''
    self.assertEqual(self.blog.title,"title")
    self.assertEqual(self.blog.body,"body")
    self.assertEqual(self.blog.date,"date")
    self.assertEqual(self.blog.category,"category")
    self.assertEqual(self.blog.img_path,"path")
    self.assertEqual(self.blog.brief,"brief")
    self.assertEqual(self.blog.authorId,2)

  



if __name__ == "__main__":
  unittest.main()