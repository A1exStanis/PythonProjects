from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('', views.show_all_movie),
  path('movie/<str:slug_movie>', views.show_one_movie, name='movie-detail'),
  path('directors/', views.show_all_directors),
  path('actors/', views.show_all_actors),
  path('actor/<int:id_actor>', views.show_one_actor, name='actor-detail'),
  path('directors/<int:id_director>', views.show_one_director, name='director-detail')
]
