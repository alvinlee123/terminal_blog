import uuid
import datetime

from database import Database
from models.post import Post

__author__ = 'alee'

class Blog(object):

    def __init__(self,author, title, description, id=None):
        self.author=author
        self.title = title
        self.description =description
        self.id=uuid.uuid4().hex if id is None else id

    def new_post(self):
        #should ask user to write new post
        title = input("Enter Post title: ")
        content= input("Enter post Content: ")
        date = input("Enter post date, or leave blank for today (in format DDMMYYYY): ")
        post = Post(blog_id=self.id,
                    title=title,
                    content=content,
                    date=datetime.datetime.strptime(date,"%d%m%Y") if date is None else date,
                    author=self.author)
        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog_id(self.id)

    def save_to_mongo(self):
        Database.insert(collection="blogs",
                        data=self.json())

    def json(self):
        return{
            "author":self.author,
            "title":self.title,
            "description":self.description,
            "id":self.id
        }
    @classmethod
    def from_mongo(cls,id):
        blog_data = Database.find_one(collection='blogs',
                                      query={'id':id})
        return cls(author=blog_data['author'],
                    title=blog_data['title'],
                    description=blog_data['description'],
                    id=blog_data['id'])