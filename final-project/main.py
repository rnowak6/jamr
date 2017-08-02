#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from google.appengine.ext import ndb
import jinja2
import os
import webapp2
import urllib2
import json
import urllib
from spotify_data_model import spotifyUserInfo
import spotipy
import sys
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import pprint
#sp = spotipy.Spotify(SpotifyClientCredentials(client_id='2121dea381d948d38a492624ddddf03a',client_secret='12197784c3434ea6b407f11b4b993c8e'))
# sp = spotipy.Spotify()

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

# client_id= os.getenv("SPOTIPY_CLIENT_ID")
# client_secret=os.getenv("SPOTIPY_CLIENT_SECRET")


class MainHandler(webapp2.RequestHandler):
    def get(self):
        # search = self.request.get("search")
        # my_template = jinja_environment.get_template("templates/test.html")
        # places_data_source = urllib2.urlopen(
        #     "https://maps.googleapis.com/maps/api/place/textsearch/json?query=subwaysinChicago&key=AIzaSyCCRonxhEphWEum0RufD1kNxAHS1ngWXO0")
        # places_json_content = places_data_source.read()
        # parsed_places_dictionary = json.loads(places_json_content)
        # results = parsed_places_dictionary["results"]

        base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
        api_key = "AIzaSyCCRonxhEphWEum0RufD1kNxAHS1ngWXO0"
        query = "places in Chicago"
        search_params = {"query": query, "key": api_key}
        search_url = base_url + urllib.urlencode(search_params)
        search_url_data_source = urllib2.urlopen(search_url)
        search_url_json_content = search_url_data_source.read()
        parsed_search_url_dictionary = json.loads(search_url_json_content)
        search_url_results = parsed_search_url_dictionary["results"]
        latlngList = []
        for result in search_url_results:
            latlngDict = result["geometry"]["location"]
            lat = latlngDict["lat"]
            lng = latlngDict["lng"]
            latlngList.append((lat,lng))
        render_data = { "lat": lat, "lng": lng, "coordinate_list" : latlngList}
        self.response.write(my_template.render(render_data))

class LocationInformationHandler(webapp2.RequestHandler):
    def get(self):
        my_template=jinja_environment.get_template("templates/LocationInformation.html")
        # information_data_source = urllib2.urlopen(
        # "https://maps.googleapis.com/maps/api/place/details/json?placeid=ChIJN1t_tDeuEmsRUsoyG83frY4&key=AIzaSyDWxfkwgYMRFBLBc5TH0pBlsjx499vk4hg"
        # )
        # information_json_content = information_data_source.read()
        # parsed_information_dictionary = json.loads(information_json_content)
        # results = parsed_information_dictionary["results"]
        base_url = "https://maps.googleapis.com/maps/api/place/details/json?"
        api_key = "AIzaSyCCRonxhEphWEum0RufD1kNxAHS1ngWXO0"
        placeid = "ChIJN1t_tDeuEmsRUsoyG83frY4"
        Info_params = {"placeid": placeid, "key": api_key}
        Info_url = base_url + urllib.urlencode(Info_params)
        Info_url_data_source = urllib2.urlopen(Info_url)
        Info_url_json_content = Info_url_data_source.read()
        parsed_Info_url_dictionary = json.loads(Info_url_json_content)
        Info_url_results = parsed_Info_url_dictionary["result"]
        nameList = []
        # hoursList = []
        for name in Info_url_results["address_components"]:
            longName = name["long_name"]
        # result == "address_components"
        # print nameDict
        # for name in nameDict:
        #     longName = name["long_name"]
            nameList.append(longName)
        render_data = {"longName": longName, "name": nameList}
        self.response.write(my_template.render(render_data))


class idHandler(webapp2.RequestHandler):
    def get(self):
        my_template=jinja_environment.get_template("templates/LocationInformation.html")
        base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
        api_key = "AIzaSyCCRonxhEphWEum0RufD1kNxAHS1ngWXO0"
        query = "places in Chicago"
        search_params = {"query": query, "key": api_key}
        search_url = base_url + urllib.urlencode(search_params)
        search_url_data_source = urllib2.urlopen(search_url)
        search_url_json_content = search_url_data_source.read()
        parsed_search_url_dictionary = json.loads(search_url_json_content)
        search_url_results = parsed_search_url_dictionary["results"]
        placeid = search_url_results["place_id"]
        render_data = {"placeid": placeid}
        self.response.write(my_template.render(render_data))



client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


class LoginHandler(webapp2.RequestHandler):
    # client_id=os.getenv("SPOTIPY_CLIENT_ID")
    # client_secret= os.getenv("SPOTIPY_CLIENT_SECRET")
    # client_credentials_manager = SpotifyClientCredentials(client_id,client_secret)
    # sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    os.environ['SPOTIPY_CLIENT_ID']='2121dea381d948d38a492624ddddf03a'
    os.environ['SPOTIPY_CLIENT_SECRET']='12197784c3434ea6b407f11b4b993c8e'
    client_id=os.environ['SPOTIPY_CLIENT_ID']
    client_secret=os.environ['SPOTIPY_CLIENT_SECRET']
    def getGenres(self):
        query=spotifyUserInfo.query()
        username=query.fetch()[3].postUserName
        playlists = sp.user_playlists(username)
        playlist=playlists['items'][0]
        length = playlist['tracks']['total']
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
        if playlist_tracks['next']:
            playlist_tracks = sp.next(playlist_tracks)
        else:
                playlist_tracks = None
        return types_of_songs

    def get(self):

        client_credentials_manager = SpotifyClientCredentials()
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        my_template=jinja_environment.get_template("templates/login.html")
        render_data={}
        username=self.request.get("username")
        if username!="":
            spotify_user=spotifyUserInfo(postUserName=username)
            spotify_user.put()
        render_data['name']=username
        render_data['genres']=self.getGenres()
        self.response.write(my_template.render(render_data))

class ServiceHandler(webapp2.RequestHandler):
    def get(self):
        my_template=jinja_environment.get_template("templates/service.html")
        render_data={}
        query = spotifyUserInfo.query()
        render_data['list_of_users'] = query.fetch()
        self.response.write(my_template.render(render_data))

class TestHandler(webapp2.RequestHandler):
    def get(self):
        spotify=spotipy.Spotify()
        results = spotify.search(q='artist:' + "Coldplay", type='artist')
        self.response.write(results)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/login',LoginHandler),
    ('/Info', LocationInformationHandler),
    ('/service',ServiceHandler),

    ('/id', idHandler)

    ('/test',TestHandler)


], debug=True)
