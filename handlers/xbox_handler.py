
import jinja_env
import logging
import webapp2

from models import book

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