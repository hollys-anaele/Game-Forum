
import jinja_env
import logging
import webapp2
import os

from google.appengine.ext import ndb


class Comment(ndb.Model):
    author = ndb.StringProperty()
    contents = ndb.StringProperty()
    animal = ndb.StringProperty()
    
class XboxHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("XboxHandler")
        comments = Comment.query().fetch()
        comment_str = ""
        for comment in comments:
            comment_str += "<div>"
            comment_str += "<h3>" + "comment by " + comment.author + ":" "</h3>"
            comment_str += "<p>" + comment.contents + "</p>"
            comment_str += "<p>" + str(comment.animal) + "</p>" #new line
            comment_str += "</div>"
       
        thing = {
            "title": "Xbox One Discussion Board",
            "html_comments": comment_str
        }
        template = jinja_env.env.get_template("templates/tmpl.html")
        self.response.out.write(template.render(thing))

       
    def post(self):
        r_author = self.request.get("forum_author")
        r_comment = self.request.get("forum_comment")
        

        new_comment = Comment(author=r_author, contents=r_comment)
        new_comment.put()
        
        self.redirect("/xbox")
        
            
        thing = {
            "html_comments": comment_str
        }
        template = jinja_env.get_template("templates/comments.html")
        self.response.out.write(template.render(thing))

    