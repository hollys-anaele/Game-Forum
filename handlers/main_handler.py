
import jinja_env
import logging
import webapp2

from google.appengine.ext import ndb
from google.appengine.api import users
import os
#from [folder] import [filename] (for author, user comment, and email
from models import author_model



#comments
class Comment(ndb.Model):
    author = ndb.StringProperty()
    contents = ndb.StringProperty()
    
class MainHandler(webapp2.RequestHandler):
    def get(self):
        logging.info(users.get_current_user())
        logging.info(users.create_login_url("/"))
        
        current_user = users.get_current_user()
        
        user_comments_query = Comment.query(Comment.author == current_user.email())
        user_comments = user_comments_query.fetch()
        logging.info(len(user_comments))
 #       userlog = len(user_comments)
        comments = Comment.query().fetch()
        comment_str = ""
        for comment in comments:
            comment_str += "<div>"
            comment_str += "<h3>User: " + comment.author + "</h3>"
            comment_str += "<p>" + comment.contents + "</p>"
            comment_str += "</div>"
            
        template = jinja_env.get_template("templates/main.html")
        
        henry = {
        "html_comments": comment_str,
        "html_login_url": users.create_login_url("/"),
        "html_userlog": len(user_comments)
        }
        
        user = users.get_current_user()
        if user != None:
            henry["html_user"] = user.email()
        
        self.response.out.write(template.render(henry))
    
    def post(self):
        author = users.get_current_user()
        if author != None:
            r_contents = self.request.get("form_contents")
            logging.info("contents was "+r_contents)

            new_comment = Comment(author=author.email(), contents=r_contents)
            new_comment.put()

        self.redirect("/")
        
        
