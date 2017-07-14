
import jinja_env
import logging
import webapp2
import os

from google.appengine.ext import ndb

#from models import book

class XboxHandler(webapp2.RequestHandler):
    def get(self):
    	#logging.info("XBONEHandler")
    	# do stuff with xbox
        html_params = {
            "title": "Xbox One Discussion Board",
            "content": "talk about xbox"
        }
        template = jinja_env.env.get_template('templates/tmpl.html')
        self.response.out.write(template.render(html_params))

        # code to make the comments work below
class Comment(ndb.Model):
    author = ndb.StringProperty()
    contents = ndb.StringProperty()
    animal = ndb.StringProperty()
    
class OtherHandler(webapp2.RequestHandler):
    def get(self):
    
        comments = Comment.query().fetch()
        comment_str = ""
        for comment in comments:
            comment_str += "<div>"
            comment_str += "<h3>" + "comment by " + comment.author + ":" "</h3>"
            comment_str += "<p>" + comment.contents + "</p>"
            comment_str += "<p>" + str(comment.animal) + "</p>" #new line
            comment_str += "</div>"
       
        thing = {
            "html_comments": comment_str
        }
        template = jinja_env.get_template("templates/comments.html")
        self.response.out.write(template.render(thing))

       
    def post(self):
        r_author = self.request.get("form_author")
        r_comment = self.request.get("form_comment")
        r_animal = self.request.get("form_animal")

        new_comment = Comment(author=r_author, contents=r_comment, animal=r_animal)
        new_comment.put()
        
        self.redirect("/xbox")
        
            
        thing = {
            "html_comments": comment_str
        }
        template = jinja_env.get_template("templates/comments.html")
        self.response.out.write(template.render(thing))

    