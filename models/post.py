import uuid
import datetime
from database import Database

__author__ = 'alee'

class Post(object):

    def __init__(self, blog_id: object, title: object, content: object, author: object,
                 date: object = datetime.datetime.utcnow(),
                 id: object = None) -> object:
        self.created_date=date
        self.id=uuid.uuid4().hex if id is None else id
        self.blog_id=blog_id
        self.title=title
        self.content=content
        self.author=author
        #post = Post(blog_id="123", title ='a title", content "some content", author "Jose", date=datetimedateimte.utcnow())

    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())

    def json(self):
        return {
            'id':self.id,
            'blog_id':self.blog_id,
            'title':self.title,
            'content':self.content,
            'author':self.author,
            'created_date':self.created_date
        }
    @classmethod
    def from_mongo(cls,id):
        #Post.from_mongo(123)
        post_data = Database.find_one(collection='posts',query={'id':id})
        return cls(blog_id= post_data['blog_id'],
                   title= post_data['title'],
                   content= post_data['content'],
                   author= post_data['author'],
                   date= post_data['date'],
                   id=post_data['id'])

    @staticmethod
    def from_blog_id(id):
        return [post for post in Database.find(collection='posts',query={'blog_id':id})]