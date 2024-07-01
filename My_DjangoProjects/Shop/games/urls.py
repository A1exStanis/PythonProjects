from django.urls import path
from games import views


urlpatterns = [
    path('hello/', views.hello),
    path('contacts/', views.contacts)
]