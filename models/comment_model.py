from google.appengine.ext import ndb

class Comment(ndb.Model):
    author = ndb.StringProperty()
    user_comment = ndb.StringProperty()
    game_name = ndb.StringProperty()
    plat_form = ndb.StringProperty()