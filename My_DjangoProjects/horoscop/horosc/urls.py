from django.urls import path
from . import views

urlpatterns = [
    path('type', views.make_types),
    path('', views.index, name='horoscope-index'),
    path('<int:month>/<int:day>', views.get_info_by_date),
    path('<int:sign_zodiac>', views.get_info_by_number),
    path('<str:sign_zodiac>', views.get_info, name='horoscope-name'),
]