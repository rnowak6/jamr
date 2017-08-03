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
from spotipyintegration import getGenres
from getTheLocation import playlistGenre
from getTheLocation import assignLocation

#sp = spotipy.Spotify(SpotifyClientCredentials(client_id='2121dea381d948d38a492624ddddf03a',client_secret='12197784c3434ea6b407f11b4b993c8e'))
# sp = spotipy.Spotify()

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

# client_id= os.getenv("SPOTIPY_CLIENT_ID")
# client_secret=os.getenv("SPOTIPY_CLIENT_SECRET")

global count
count=0

def get_max_number():
    q = spotifyUserInfo.query()
    f_q=q.fetch()
    user_numbers=[]
    for i in range(len(f_q)):
        user_numbers.append(f_q[i].userNumber)
    max_user_num=0
    for num in user_numbers:
        if num>max_user_num:
            max_user_num=num
    return max_user_num

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # search = self.request.get("search")
        my_template = jinja_environment.get_template("Templates/test.html")
        # places_data_source = urllib2.urlopen(
        #     "https://maps.googleapis.com/maps/api/place/textsearch/json?query=subwaysinChicago&key=AIzaSyCCRonxhEphWEum0RufD1kNxAHS1ngWXO0")
        # places_json_content = places_data_source.read()
        # parsed_places_dictionary = json.loads(places_json_content)
        # results = parsed_places_dictionary["results"]
        q = spotifyUserInfo.query()
        f_q=q.fetch()
        user_numbers=[]
        for i in range(len(f_q)):
            user_numbers.append(f_q[i].userNumber)
        max_user_num=get_max_number()
        print max_user_num
        # for num in user_numbers:
        #     if num>max_user_num:
        #         max_user_num=num
        for i in range(len(f_q)):
            if f_q[i].userNumber==max_user_num:
                query=f_q[i].location
        base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
        api_key = "AIzaSyAjMkxmL8taLeHU2oaENqmsZngProCoXaM"
        #query = "high schools"
        search_params = {"query": query, "key": api_key}
        search_url = base_url + urllib.urlencode(search_params)
        search_url_data_source = urllib2.urlopen(search_url)
        search_url_json_content = search_url_data_source.read()
        parsed_search_url_dictionary = json.loads(search_url_json_content)
        search_url_results = parsed_search_url_dictionary["results"]
        # print search_url_results
        placeidList = []
        for search in search_url_results:
            placeid = search["place_id"]
            placeidList.append(placeid)
        nameList = []
        phoneList = []
        addressList = []
        for placeid in placeidList:
            base_url = "https://maps.googleapis.com/maps/api/place/details/json?"
            api_key = "AIzaSyAjMkxmL8taLeHU2oaENqmsZngProCoXaM"
            placeid = placeid
            Info_params = {"placeid": placeid, "key": api_key}
            Info_url = base_url + urllib.urlencode(Info_params)
            Info_url_data_source = urllib2.urlopen(Info_url)
            Info_url_json_content = Info_url_data_source.read()
            parsed_Info_url_dictionary = json.loads(Info_url_json_content)
            Info_url_results = parsed_Info_url_dictionary["result"]
            # hoursList = []
            # for name in Info_url_results["name"]:
            thingName = Info_url_results["name"]
            # nameList.append(thingName)
            # placePhone = phoneNumber
            #placePhone = Info_url_results["formatted_phone_number"]
            # phoneList.append(placePhone)
            # nameList.append(placePhone)
            # for addressName in Info_url_results["formatted_address"]:
            address = Info_url_results["formatted_address"]
            # addressList.append(longName)
            nameList.append((thingName, address))
            #nameList.append((thingName, address, placePhone))




        latlngList = []
        for result in search_url_results:
            latlngDict = result["geometry"]["location"]
            lat = latlngDict["lat"]
            lng = latlngDict["lng"]
            latlngList.append((lat,lng))
        # render_data = { "lat": lat, "lng": lng, "coordinate_list" : latlngList}
        #render_data = { "lat": lat, "lng": lng, "coordinate_list" : latlngList, "thingName": thingName, "address": address, "placePhone": placePhone, "name": nameList}
        render_data = { "lat": lat, "lng": lng, "coordinate_list" : latlngList, "thingName": thingName, "address": address, "name": nameList}

        self.response.write(my_template.render(render_data))

class LocationInformationHandler(webapp2.RequestHandler):
    def get(self):
        my_template=jinja_environment.get_template("Templates/LocationInformation.html")
        base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
        api_key = "AIzaSyAjMkxmL8taLeHU2oaENqmsZngProCoXaM"
        query = "high schools"
        search_params = {"query": query, "key": api_key}
        search_url = base_url + urllib.urlencode(search_params)
        search_url_data_source = urllib2.urlopen(search_url)
        search_url_json_content = search_url_data_source.read()
        parsed_search_url_dictionary = json.loads(search_url_json_content)
        search_url_results = parsed_search_url_dictionary["results"]
        # print search_url_results
        placeidList = []
        for search in search_url_results:
            placeid = search["place_id"]
            placeidList.append(placeid)
        nameList = []
        phoneList = []
        addressList = []
        for placeid in placeidList:
            base_url = "https://maps.googleapis.com/maps/api/place/details/json?"
            api_key = "AIzaSyAjMkxmL8taLeHU2oaENqmsZngProCoXaM"
            placeid = placeid
            Info_params = {"placeid": placeid, "key": api_key}
            Info_url = base_url + urllib.urlencode(Info_params)
            Info_url_data_source = urllib2.urlopen(Info_url)
            Info_url_json_content = Info_url_data_source.read()
            parsed_Info_url_dictionary = json.loads(Info_url_json_content)
            Info_url_results = parsed_Info_url_dictionary["result"]
            # hoursList = []
            # for name in Info_url_results["name"]:
            thingName = Info_url_results["name"]
            # nameList.append(thingName)
            # placePhone = phoneNumber
            placePhone = Info_url_results["formatted_phone_number"]
            # phoneList.append(placePhone)
            # nameList.append(placePhone)
            # for addressName in Info_url_results["formatted_address"]:
            address = Info_url_results["formatted_address"]
            # addressList.append(longName)
            nameList.append((thingName, address, placePhone))
        render_data = {"thingName": thingName, "address": address, "placePhone": placePhone, "name": nameList}
        self.response.write(my_template.render(render_data))

class idHandler(webapp2.RequestHandler):
    def get(self):
        my_template=jinja_environment.get_template("Templates/id.html")
        base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
        api_key = "AIzaSyCCRonxhEphWEum0RufD1kNxAHS1ngWXO0"
        query = "places in Chicago"
        search_params = {"query": query, "key": api_key}
        search_url = base_url + urllib.urlencode(search_params)
        search_url_data_source = urllib2.urlopen(search_url)
        search_url_json_content = search_url_data_source.read()
        parsed_search_url_dictionary = json.loads(search_url_json_content)
        search_url_results = parsed_search_url_dictionary["results"]
        # print search_url_results
        placeidList = []
        for search in search_url_results:
            placeid = search["place_id"]
            placeidList.append(placeid)
        render_data = { "placeidList": placeidList}
        # render_data = {"placeidList": search_url_results}
        self.response.write(my_template.render(render_data))



client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)



def return_count():
    global count
    return count

def update_count():
    global count
    count+=1
    return count

class LoginHandler(webapp2.RequestHandler):
    # client_id=os.getenv("SPOTIPY_CLIENT_ID")
    # client_secret= os.getenv("SPOTIPY_CLIENT_SECRET")
    # client_credentials_manager = SpotifyClientCredentials(client_id,client_secret)
    # sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    os.environ['SPOTIPY_CLIENT_ID']='2121dea381d948d38a492624ddddf03a'
    os.environ['SPOTIPY_CLIENT_SECRET']='12197784c3434ea6b407f11b4b993c8e'
    client_id=os.environ['SPOTIPY_CLIENT_ID']
    client_secret=os.environ['SPOTIPY_CLIENT_SECRET']

    def get(self):
        my_template=jinja_environment.get_template("Templates/login.html")
        render_data={}
        username=self.request.get("username")

        render_data['name']=username
        render_data['genres']=getGenres(username)
        render_data['maxGenre']=playlistGenre(render_data['genres'])
        render_data['location']=assignLocation(render_data['maxGenre'])
        if username!="":
            spotify_user=spotifyUserInfo(postUserName=username,location=render_data['location'],userNumber=get_max_number()+1)
            spotify_user.put()
            update_count()
        self.response.write(my_template.render(render_data))


class ServiceHandler(webapp2.RequestHandler):
    def get(self):
        my_template=jinja_environment.get_template("Templates/service.html")
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
    ('/id', idHandler),
    ('/test',TestHandler)

], debug=True)
