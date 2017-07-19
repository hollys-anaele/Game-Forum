
import jinja_env
import logging
import webapp2
import os

from google.appengine.ext import ndb
from google.appengine.api import users
from models import comment_model
                     
                     
class PS4Handler(webapp2.RequestHandler):
    def get(self):
   #     "title": "PS4 Discussion Board",
    	logging.info("PS4Handler")
        logging.info(users.get_current_user())
        logging.info(users.create_login_url('/ps4'))
        comments = comment_model.Comment.query(comment_model.Comment.plat_form == "PS4").fetch()
        comment_str = ""
        for comment in comments:
            comment_str += "<div>"
            
            str(comment.plat_form) + "</b>" + "</p>" 
            comment_str += "<p>" + "<b>" + "About the game: " + str(comment.game_name) + "</b>" + "</p>" 
            comment_str += "<h3>" + "Post by " + comment.author + ":" "</h3>"    
            comment_str += "<p>" + str(comment.user_comment) + "</p>"
            comment_str += "</div>"
        template = jinja_env.env.get_template("templates/ps4.html")
        thing = {
            "html_comments2": comment_str,
            "html_login_url2": users.create_login_url('/ps4'),
        }
        
        self.response.out.write(template.render(thing))
    def post(self):
        user = users.get_current_user()
        if user != None: 

            r2_comment = self.request.get("form2_comment")
            r2_game = self.request.get("form2_game")
            r2_platform = self.request.get("form2_platform")

            new_comment = comment_model.Comment(author=user.email(), user_comment=r2_comment, game_name=r2_game, plat_form=r2_platform)
            new_comment.put()
        
        self.redirect("/ps4")
        


