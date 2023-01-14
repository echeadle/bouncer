from google.cloud import ndb
from app.datastore import get_client
from bouncer.models import Redirect

client = get_client()

with client.context():
    key = ndb.Key(Redirect, 'sample-redirect')
    redirect = Redirect(key=key, name='Sample Redirect',  destination_url='https://example.com')
    redirect.put()


  docker compose run --rm app sh -c "python manage.py shell"

with client.context():
    redirects = Redirect.query().fetch()
    for r in redirects:
        print(f'Key: {r.key}')
        print(f'Dest: {r.destination_url}')