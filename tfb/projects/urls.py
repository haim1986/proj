from django.urls import path, re_path
from . import views


urlpatterns = [
    #projects:
    path('', views.index, name='index'),
    #projects/movie_id/:
    re_path(r'^(?P<movie_id>[0-9]+)/$', views.moviesDetails, name="moviesDetails"),

    #projects/movie_id/favorite:
     re_path(r'^(?P<movie_id>[0-9]+)/favorite$', views.favorite, name="fbfavorite"),
    ]

