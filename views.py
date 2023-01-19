"""
Main view functions for handling requests.
"""

from google.cloud import ndb

from django.shortcuts import (
    render,
    redirect,
)
from django.http import Http404

from bouncer.models import Redirect


def landing(request):
    """Render the landing page."""
    redirects = Redirect.query().fetch()

    return render(request, 'bouncer/index.html', {'redirects': redirects})


def handle_redirect(request, slug):
    """Handle a redirect."""
    redirect_entity = ndb.Key(Redirect, slug).get()
    if not redirect_entity:
        raise Http404('Not found')

    return redirect(redirect_entity.destination_url, permanent=True)
