
import jinja_env
import logging
import webapp2

class AboutHandler(webapp2.RequestHandler): #the about page
    def get(self):
    	logging.info("AboutHandler")
        html_params = {
            "title": "About",
            "content": "This is the about page. Our website is dedicated to provide a forum for individuals to talk about their favourite game consoles and video games freely."
        }
        template = jinja_env.env.get_template('templates/tmpl.html')
        self.response.out.write(template.render(html_params))