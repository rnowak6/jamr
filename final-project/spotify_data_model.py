from google.appengine.ext import ndb

class spotifyUserInfo(ndb.Model):
    postUserName = ndb.StringProperty()
    playlist_genre = ndb.StringProperty()
    locations = ndb.StringProperty(repeated =True)
