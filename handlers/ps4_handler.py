
import jinja_env
import logging
import webapp2

class PS4Handler(webapp2.RequestHandler): #the bio page
    def get(self):
    	logging.info("PS4Handler")
        html_params = {
            "title": "PS4 Discussion Board",
            "content": "Say some stuff about ps4 games"
        }
        template = jinja_env.env.get_template('templates/tmpl.html')
        self.response.out.write(template.render(html_params))