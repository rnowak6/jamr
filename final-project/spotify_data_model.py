from google.appengine.ext import ndb

class spotifyUserInfo(ndb.Model):
    userName = ndb.StringProperty()
    playlist_genre = ndb.StringProperty()
    locations = ndb.StringProperty(repeat=True)
