# Cheatsheet

## Docker Compose Commands

### Django Commands

Create Django project:

```sh
docker-compose run --rm app sh -c "django-admin startproject app ."
```

Start app called `bouncer`:

```sh
docker-compose run --rm app sh -c "python manage.py startapp bouncer
```

Run development server:

```sh
docker-compose up
```

### Deployment Commands

Check version of CloudSDK:

```sh
docker-compose -f docker-compose-deploy.yml run gcloud gcloud version
```

Authenticate with Google Cloud Platform (GCP):

```sh
docker-compose -f docker-compose-deploy.yml run gcloud gcloud auth login
```

Deploy to GAE:

 * Replace `PROJECT_ID` with your Google Cloud Project ID.

```sh
docker-compose run --rm app sh -c "python manage.py collectstatic --noinput"
docker-compose -f docker-compose-deploy.yml run gcloud gcloud app deploy --project PROJECT_ID
```

## Django Shell Datastore

### Creating an Entity

To create a new `Redirect` entity, enter the Django shell by running:

```sh
docker-compose run --rm app sh -c "python manage.py shell"
```

In the interactive shell, run the following:

```python
from google.cloud import ndb
from app.datastore import get_client
from bouncer.models import Redirect
 
client = get_client()

with client.context():
    key = ndb.Key(Redirect, 'sample-redirect')
    redirect = Redirect(key=key, name='Sample Redirect', destination_url='https://example.com')
    redirect.put()
```

To retrieve an entity, run the following:

```python
from google.cloud import ndb
from app.datastore import get_client
from bouncer.models import Redirect
 
client = get_client()

with client.context():
    redirects = Redirect.query().fetch()
    for r in redirects:
        print(f'Key: {r.key}')
        print(f'Dest: {r.destination_url}')
 
```

Note: You need to hit enter twice after the final line.
