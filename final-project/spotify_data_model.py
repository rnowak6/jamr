from google.appengine.ext import ndb

class spotifyUserInfo(ndb.Model):
    postUserName = ndb.StringProperty()
    playlist_genre = ndb.StringProperty()
    location = ndb.StringProperty()
