from django.urls import path
from .views import calc_view


urlpatterns = [
    path('', calc_view, name="calc"),
]