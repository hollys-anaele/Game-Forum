
import jinja_env
import logging
import webapp2

from google.appengine.ext import ndb
from google.appengine.api import users
import os

class Comment(ndb.Model):
    author = ndb.StringProperty()
    contents = ndb.StringProperty()


class MainHandler(webapp2.RequestHandler): #the about page
    def get(self):
        logging.info("MainHandler")
        html_params = {
            "title": "Arcade Crawlers",
            "content": "Hello"
        }
        


        current_user = users.get_current_user()
        logging.info(users.get_current_user())
        logging.info(users.create_login_url("/"))
       

        template = jinja_env.env.get_template('templates/main.html')
        self.response.out.write(template.render(html_params))
        
        
        #trying to make if user is logged in redirect to home page 
        
        # #if current_user != None:
        #    user_comments_query = Comment.query(Comment.author == current_user.email())
        # else: 
        #     self.redirect("/") #redirects back to this page
        #     return 
        
        
        #user_forum = user_comments_query.fetch()
        #logging.info(len(user_forum))
        #forum_post =  Comment.query().fetch()


        # forum_str = " "
        # for comment in forum_post:
        #     forum_str += "<div>"
        #     forum_str += "<h3>" + comment.author + "</h3>"
        #     forum_str += "<p> " + comment.contents + "</p>"
        #     forum_str += "<h4>" + str(comment.fav_animal) + "</h4>"
        #     forum_str += "</div>"

            #template = jinja_environment.get_template("templates/comments.html")

    #     henry ={
    #     "html_comments": forum_str,
    #     "html_login_url": users.create_login_url("/rachel"),
    #     "user": user.get_current_user(),
    #     "count_comment": len(user_forum)
    #     }
    #     if current_user != None:
    #         henry["html_user"] = current_user.email()
        
    #     self.response.out.write(template.render(henry))
    # def post(self):
    #     author_name = users.get_current_user()
    #     r_comment = self.request.get("form_comment")
    #     logging.info("Comment " + r_comment) 
    #     new_comment = Comment(author = author_name.email(), contents = r_comment, fav_animal = r_animal_content)
