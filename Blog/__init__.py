from datetime import datetime
from Blog import app
from .app import db
#from .models.setdb import create_db
#from Blog.models.blog import Blog
from .models.models import Comment,Blog
from .models.writer import Writer

# print("model")
# db.create_all()
# db.session.commit()



# newPost = Blog("m1 Chip","this is a cool processor",datetime.today(),"Gadgets","https://cdn.vox-cdn.com/thumbor/xLToiRTDVy9o0IU4VMegkSz_nO4=/0x0:2040x1358/920x613/filters:focal(857x516:1183x842):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/69195508/vpavic_4291_20201113_0337_Edit.0.jpg","apples chip",1)
# db.session.add(newPost)
# db.session.commit()




