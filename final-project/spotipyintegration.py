import spotipy
import pprint
import sys
import spotipy.util as util
import os
from spotipy.oauth2 import SpotifyClientCredentials
import json
#from google.appengine.ext import ndb
#from spotify_data_model import spotifyUserInfo


#my_user=spotifyUserInfo(postUserName=amelialutz9)
#print client_credentials_manager

# user=raw_input("Username: ")
def getGenres(user):
    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    playlists = sp.user_playlists(user)
    playlist=playlists['items'][0]
    length = playlist['tracks']['total']
        #print playlist
    #print length
    playlist_name=playlists['items'][0]['name']
    #print playlist_name
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

        #for i in range(len(artists)):
            #print "%s. %s-%s"%(i+1,artists[i],types_of_songs[i])
    if playlist_tracks['next']:
        playlist_tracks = sp.next(playlist_tracks)
    else:
        playlist_tracks = None
    return types_of_songs

print getGenres(user)
# user=raw_input("Username: ")
# print getGenres(user)
>>>>>>> c75d5aa9cc6054868d8c3c28a7cadc46a5467c37
