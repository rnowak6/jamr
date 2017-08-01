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
# import spotipy
# import sys
# import spotipy.util as util

# sp = spotipy.Spotify()

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # search = self.request.get("search")
        my_template = jinja_environment.get_template("templates/test.html")
<<<<<<< HEAD
        places_data_source = urllib2.urlopen(
            "https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants%20in%20chicago&key=AIzaSyDWxfkwgYMRFBLBc5TH0pBlsjx499vk4hg")
        places_json_content = places_data_source.read()
        parsed_places_dictionary = json.loads(places_json_content)
        latlngDict = parsed_places_dictionary["results"][0]["geometry"]["location"]
        lat = latlngDict["lat"]
        lng = latlngDict["lng"]
        render_data = { "lat": lat, "lng": lng}
        self.response.write(my_template.render(render_data))

        # url_params = {'q': search, 'api_key': 'dc6zaTOxFJmzC', 'limit': 10}
        #     giphy_response = urllib2.urlopen(base_url + urllib.urlencode(url_params)).read()
        #     parsed_giphy_response_dictionary = json.loads(giphy_response)
        #     giphy_url = parsed_giphy_response_dictionary['data'][i]['images']['original']['url']
        #     render_data = { "image": gif_url, "image2": giphy_url}
        #     # self.response.write(my_template.render(gif_url))
        #     self.response.write(my_template.render(render_data))
        #     # self.response.write(gif_url)


# class AmeliaHandler(webapp2.RequestHandler):
=======
        self.response.write(my_template.render())

# class LoginHandler(webabb2.RequestHandler):
>>>>>>> 66c3a0e7ff3033229f05b8c89793785ae9920ccc
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
<<<<<<< HEAD
=======
#         self.response.write("this is loaded")
>>>>>>> 66c3a0e7ff3033229f05b8c89793785ae9920ccc


app = webapp2.WSGIApplication([
    ('/', MainHandler),
<<<<<<< HEAD
    # ('/Amelia', AmeliaHandler)
=======
    ('/login',LoginHandler)
>>>>>>> 66c3a0e7ff3033229f05b8c89793785ae9920ccc
], debug=True)
