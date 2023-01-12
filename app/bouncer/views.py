from django.shortcuts import render


def landing(request):
    """Render the Landing page."""
    return render(request, 'bouncer/index.html')
