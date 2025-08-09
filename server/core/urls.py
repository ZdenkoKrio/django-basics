from django.urls import path
from .views import (home, home2, home_d, home2_d,
                    about, random_view)


urlpatterns = [
    path('home/', home),
    path('home_d/<number>', home_d),
    path('home2/', home2),
    path('home2_d/<number>', home2_d),
    path('about/', about),
    path('random_view/', random_view),
]