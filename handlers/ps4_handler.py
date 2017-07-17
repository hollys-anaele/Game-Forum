
import jinja_env
import logging
import webapp2
import os

from google.appengine.ext import ndb

class PS4Handler(webapp2.RequestHandler): #the bio page
    def get(self):
        logging.info("PS4Handler")
        html_params = {
            "title": "PS4 Discussion Board",
            "content": "This page is dedicated to discussing specifically Playstation 4 and games."
        }
        template = jinja_env.env.get_template('templates/tmpl.html')
        self.response.out.write(template.render(html_params))
