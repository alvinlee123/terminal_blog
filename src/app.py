from database import Database
from models.blog import Blog
__author__ = 'alee'

Database.initialize()

blog = Blog(author="Alvin",
            title="Test",
            description="whatever")

blog.new_post()

blog.save_to_mongo()

from_database = Blog.from_mongo(blog.id)
print (from_database)
print(blog.get_posts())