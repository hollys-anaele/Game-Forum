
import jinja_env
import logging
import webapp2

class MainHandler(webapp2.RequestHandler): #the about page
    def get(self):
    	logging.info("MainHandler")
        html_params = {
            "title": "Main Title",
            "content": "Hello"
        }
        template = jinja_env.env.get_template('templates/tmpl.html')
        self.response.out.write(template.render(html_params))

  #      current_user = users.get_current_user()
  #      logging.info(users.get_current_user())
  #      logging.info(users.create_login_url("/rachel"))
  #      self.response.out.write('<h1> This is different</h1>')
  #      user_comments_query = Comment.query(Comment.author == current_user.email())
  #      user_comments = user_comments_query.fetch()
  #      logging.info(len(user_comments))
  #      comments =  Comment.query().fetch()