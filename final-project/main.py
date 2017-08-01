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
import spotipy
import sys
import spotipy.util as util

# sp = spotipy.Spotify()

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        my_template = jinja_environment.get_template("templates/test.html")
        self.response.write(my_template.render())

class LoginHandler(webabb2.RequestHandler):
    def get(self):
        scope = 'user-library-read'

        if len(sys.argv) > 1:
            username = sys.argv[1]
        else:
            print "Usage: %s username" % (sys.argv[0],)
            sys.exit()

        token = util.prompt_for_user_token(username, scope)

        if token:
            sp = spotipy.Spotify(auth=token)
            results = sp.current_user_saved_tracks()
            for item in results['items']:
                track = item['track']
                print track['name'] + ' - ' + track['artists'][0]['name']
        else:
            print "Can't get token for", username
        self.response.write("this is loaded")


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/login',LoginHandler)
], debug=True)
