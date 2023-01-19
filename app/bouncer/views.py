"""
Main view functions for handling requests.
"""

from google.cloud import ndb

from django.shortcuts import (
        render,
        redirect,
)

from bouncer.models import Redirect


def landing(request):
    """Render the landing page."""
    redirects = Redirect.query().fetch()

    return render(request, 'bouncer/index.html', {'redirects': redirects})


def handle_redirect(request, slug):
    """Handle a redirect."""
    pass
