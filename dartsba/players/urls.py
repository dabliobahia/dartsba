from django.urls import path
from . import views

app_name = 'players'
urlpatterns = [
    path('/player/subscribe', views.subscribe, name='subscribe'),
    path('/player/update', views.update, name='update'),
    path('player/delete', views.delete, name='delete'),
]