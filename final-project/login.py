<<<<<<< HEAD
# from google.appengine.ext import ndb
# import jinja2
# import os
# import webapp2
# import urllib2
# import json
# import urllib
# import spotipy
# import sys
# import spotipy.util as util
#
# class loginHandler(webabb2.RequestHandler):
#     def get(self):
#         scope = 'user-library-read'
#
#         if len(sys.argv) > 1:
#             username = sys.argv[1]
#         else:
#             print "Usage: %s username" % (sys.argv[0],)
#             sys.exit()
#
#         token = util.prompt_for_user_token(username, scope)
#
#         if token:
#             sp = spotipy.Spotify(auth=token)
#             results = sp.current_user_saved_tracks()
#             for item in results['items']:
#                 track = item['track']
#                 print track['name'] + ' - ' + track['artists'][0]['name']
#         else:
#             print "Can't get token for", username
=======
import spotipy
import pprint
import sys
import spotipy.util as util
import os
from spotipy.oauth2 import SpotifyClientCredentials
import json

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

user=raw_input("What is your username?")
playlists = sp.user_playlists(user)
playlist=playlists['items'][0]
length = playlist['tracks']['total']
print playlist
print length
playlist_name=playlists['items'][0]['name']
print playlist_name
playlist_tracks=sp.user_playlist_tracks(user,playlist['uri'],limit=100,offset=0)
artists=[]
types_of_songs=[]
for i in range(length):
    artist_name= playlist_tracks['items'][i]['track']['artists'][0]['name']
    artist_id= playlist_tracks['items'][i]['track']['artists'][0]['id']
    artist_genre=sp.artist(artist_id)['genres']
    if (artist_genre!=[]):
        types_of_songs.append(artist_genre[0])
    else:
        types_of_songs.append(None)
    artists.append(artist_name)

for i in range(len(artists)):
    print "%s. %s-%s"%(i+1,artists[i],types_of_songs[i])
if playlist_tracks['next']:
    playlist_tracks = sp.next(playlist_tracks)
else:
        playlist_tracks = None
print types_of_songs
>>>>>>> bb02512916c9dc2ff6069445c845680c70eeda72
