
import jinja_env
import logging
import webapp2
import os

from google.appengine.ext import ndb
                     

class Comment(ndb.Model):
    author = ndb.StringProperty()
    user_comment = ndb.StringProperty()
    game_name = ndb.StringProperty()

                     
class PS4Handler(webapp2.RequestHandler):


    def get(self):
   #     "title": "PS4 Discussion Board",
    	logging.info("PS4Handler")
        comments = Comment.query().fetch()
        comment_str = ""
        for comment in comments:
            comment_str += "<div>"
            comment_str += "<h3>" + "Post by " + comment.author + ":" "</h3>"
            comment_str += "<p>" + str(comment.user_comment) + "</p>"
            comment_str += "<p>" + str(comment.game_name) + "</p>" 
            comment_str += "</div>"
       
        thing = {
            "html_comments": comment_str
        }
        template = jinja_env.env.get_template("templates/tmpl.html")
        self.response.out.write(template.render(thing))



       
    def post(self):
        r_author = self.request.get("author")
        r_comment = self.request.get("comment")
        r_game = self.request.get("game")
        

        new_comment = Comment(author=r_author, user_comment=r_comment, game_name=r_game)
        new_comment.put()
        
        self.redirect("/ps4")
        


