from google.appengine.ext import ndb

class spotifyUserInfo(ndb.Model):
    postUser = ndb.KeyProperty()
    postUserName = ndb.StringProperty()
    playlist = ndb.KeyProperty()
    # description = ndb.StringProperty()
