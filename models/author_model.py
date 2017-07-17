from google.appengine.ext import ndb

class Author(ndb.Model):
    author = ndb.StringProperty()
    user_comment = ndb.StringProperty()
    user_email = ndb.StringProperty()