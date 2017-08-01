from google.appengine.ext import ndb

class gmapsData(ndb.Model):
    past_locations = ndb.StringProperty()
    #Location property?
    recommended_locations = ndb.StringProperty()
    # recommended_activities = ndb.StringProperty()
