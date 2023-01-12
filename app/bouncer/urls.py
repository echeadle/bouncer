"""
URL Mappings for Bouncer
"""
from django.urls import path

from bouncer import views

app_name = 'bouncer'

urlpatterns = {
    path('', views.landing, name='landing'),
}