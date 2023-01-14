"""
Datastore Models
"""

from google.cloud import ndb

class Redirect(ndb.Model):
    """Redirect Model"""
    name = ndb.StringProperty()
    destination_url = ndb.StringProperty()
    created_on = ndb.DateTimeProperty(auto_now=True)    
