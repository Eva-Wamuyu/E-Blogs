import os

class Config():

   basedirectory =os.path.abspath(os.path.dirname(__file__))
   SQLALCHEMY_DATABASE_URI = "sqlite://"+os.path.join(basedirectory,'database.sqlite')
   SQLALCHEMY_TRACK_MODIFICATIONS = False
   SECRET_KEY = os.environ.get('SECRET_KEY')

class DevConfig(Config):

  Debug = True
  pass

class ProdConfig(Config):
    
    pass


config_options = {
  'dev' : DevConfig,
  'prod' : ProdConfig,
  
}