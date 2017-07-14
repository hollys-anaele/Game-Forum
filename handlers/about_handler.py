
import jinja_env
import logging
import webapp2

class AboutHandler(webapp2.RequestHandler): #the about page
    def get(self):
    	logging.info("AboutHandler")
        html_params = {
            "title": "About",
            "content": "This is the about page. Our website is dedicated to provide a forum for individuals to discuss their favourite game consoles and video games freely.<br>We host a multitude of categories, all regarding the video game industry. The main consoles hosted here are Playstation 4, XBox One, and a combination of both. </br><br>The creators of this website, Arcade Crawlers, are students of Google highly dedicated to attaining a career in Computer Science. Quincy Blackston, Steven Hodge, <br> and Hollys Anaele, are all proud to have made this page for your convenience.</br><br>Thank you, and happy posting!</br>"


 

        }
        template = jinja_env.env.get_template('templates/tmpl.html')
        self.response.out.write(template.render(html_params))