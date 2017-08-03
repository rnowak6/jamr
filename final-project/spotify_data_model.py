from google.appengine.ext import ndb

class spotifyUserInfo(ndb.Model):
    postUserName = ndb.StringProperty()
    userNumber = ndb.IntegerProperty()
    location = ndb.StringProperty()
