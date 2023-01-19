"""
URL Mappings for bouncer.
"""
from django.urls import path

from bouncer import views


app_name = 'bouncer'


urlpatterns = [
    path('<str:slug>/', views.handle_redirect, name='redirect'),
    path('', views.landing, name='landing'),
]
