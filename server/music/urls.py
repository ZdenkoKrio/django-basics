from django.urls import path
from .views import band_list_view


urlpatterns = [
    path('list/', band_list_view, name="bands"),
]