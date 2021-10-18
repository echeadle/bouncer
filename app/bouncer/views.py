from django.shortcuts import render

# Create your views here.

def landing(request):
  """Render the landing page."""
  return render(request, 'bouncer/index.html')
