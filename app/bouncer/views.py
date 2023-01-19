"""
Main view functions for handling requests.
"""
from django.shortcuts import render

from bouncer.models import Redirect


def landing(request):
    """Render the Landing page."""
    redirects = Redirect.query().fetch()

    return render(request, 'bouncer/index.html', {'redirects': redirects})


def handle_redirect(request, slug):
    """Handle a redirect."""
    pass