
import jinja_env
import logging
import webapp2
import os

from google.appengine.ext import ndb
from google.appengine.api import users
from models import comment_model


    
class XboxHandler(webapp2.RequestHandler):
    def get(self):
   #     "title": "xbox Discussion Board",
    	logging.info("XboxHandler")
        logging.info(users.get_current_user())
        logging.info(users.create_login_url('/xbox'))
        comments = comment_model.Comment.query(comment_model.Comment.plat_form == "Xbox").fetch()
        comment_str = ""
        for comment in comments:
            comment_str += "<div>"
            str(comment.plat_form) + "</b>" + "</p>" 
            comment_str += "<h3>" "<p>" + "<b>" + "About the game: " + str(comment.game_name) + "</b>" + "</p>" "</h3>" 
            comment_str += "<h4>" + "Post by " + comment.author + ":" "</h4>" 
            comment_str += "<p>" + str(comment.user_comment) + "</p>"
            comment_str += "</div>"
       
        template = jinja_env.env.get_template("templates/xbox.html")
        thing = {
            "html_comments": comment_str,
            "html_login_url": users.create_login_url('/xbox'),
        }
        self.response.out.write(template.render(thing))
               
    def post(self):
        user = users.get_current_user()
        if user != None:
            r_comment = self.request.get("form_comment")
            r_game = self.request.get("form_game")
            r_platform = self.request.get("form_platform")
        
            new_comment = comment_model.Comment(author=user.email(), user_comment=r_comment, game_name=r_game, plat_form=r_platform)
            new_comment.put()
        self.redirect("/xbox")
        
       

    