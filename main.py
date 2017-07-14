
#import jinja2
import logging
import webapp2
import os

from google.appengine.ext import ndb

from handlers import jinja_env
from handlers import main_handler
from handlers import xbox_handler
from handlers import bio_handler
from handlers import about_handler
from handlers import ps4_handler

jinja_env.init(os.path.dirname(__file__))
logging.info("THIS IS A THING")
logging.info(jinja_env.env)

app = webapp2.WSGIApplication([
    ('/', main_handler.MainHandler),
    ('/xbox', xbox_handler.XboxHandler),
    ('/bio', bio_handler.BioHandler),
    ('/about', about_handler.AboutHandler),
    ('/ps4', ps4_handler.PS4Handler),
], debug=True)
