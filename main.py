import os
import webapp2
import logging

from handlers import jinja_env
from handlers import main_handler
from handlers import xbox_handler
from handlers import bio_handler
from handlers import about_handler
from handlers import ps4_handler

jinja_env.init(os.path.dirname(__file__))

app = webapp2.WSGIApplication([
    ('/', main_handler.MainHandler),
    ('/xbox', xbox_handler.XboxHandler),
    ('/bio', bio_handler.BioHandler),
    ('/about', about_handler.AboutHandler),
    ('/ps4', ps4_handler.PS4Handler),
], debug=True)
