from google.appengine.ext import ndb

class GMessages(ndb.Model):
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    text = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
