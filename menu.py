from database import Database
from models.blog import Blog

__author__ = 'alee'

class Menu(object):
    def __init__(self):
        #ask user for author name
        self.user = input("enter your author name" )
        self.user_blog = None
        #check if they already have account
        if self._user_has_account():
            print("Welcome back {}".format(self.user))
        else:
            self._prompt_user_for_account()
        #if not, prompt them to create one
    def _user_has_account(self):
        blog = Database.find_one('blogs',{'author':self.user})
        if blog is not None:
            self.user_blog = blog
            return True
        else:
            return False


    def _prompt_user_for_account(self):
        title = input("Enter Blog Title: ")
        description = input("Enter Blog Description: ")
        blog = Blog(author=self.user,
                    title=title,
                    description=description)
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        #user read or write blogs?
        read_or_write = input("Do you want to read(R) or write(W)? ")
        if read_or_write =='R':
            self._list_blogs()
            self._view_blog()
        #if read:
            #list blogs in database
            #allow user to pick one
            #display posts
        elif read_or_write=='W':
            self.user_blog.new_post()

        #if write:
            #check if user has a blog
            #if they do, prompt to write post
            #if not, prompt to create new blog
        else:
            print("Thanks for blogging!")

    def _list_blogs(self):
        blogs = Database.find(collection='blogs',
                              query={})
        for blog in blogs:
            print ("ID: {}, Title {}, Author {}".format(blog['id'],blog['title'],blog['author']))

    def _view_blog(self):
        blog_to_see = input("Enter ID of blog you want to see: ")
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_posts()
        for post in posts:
            print("Date: {}, title: {}\n\n{}".format(post['created_date'],post['title'],post['content']))
