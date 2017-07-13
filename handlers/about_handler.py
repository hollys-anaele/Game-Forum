
import jinja_env
import logging
import webapp2

class AboutHandler(webapp2.RequestHandler): #the about page
    def get(self):
    	logging.info("AboutHandler")
        html_params = {
            "title": "About",
            "content": "This is the about page test"
        }
        template = jinja_env.env.get_template('templates/tmpl.html')
        self.response.out.write(template.render(html_params))