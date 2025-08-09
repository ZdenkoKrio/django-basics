from django.urls import path
from .views import (home, home2, home_d, home2_d,
                    about, random_view, random_view2, random_view3)


urlpatterns = [
    path('home/', home),
    path('home_d/<number>', home_d),
    path('home2/', home2),
    path('home2_d/<number>', home2_d),
    path('about/', about),
    path('random_view/<int:start>/<int:end>', random_view2),
    path('random_view/', random_view),
    path('random_view/<int:start>/<int:end>/<int:turns>', random_view3),
]