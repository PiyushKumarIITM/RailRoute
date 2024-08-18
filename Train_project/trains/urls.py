# trains/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('find-route/', views.find_route_view, name='find_route_view'),
    path('find-route-submit/', views.find_route, name='find_route'),
]
