from django.urls import path
from .views import (band_list_view, band_detail_view, band_create_view,
                    album_detail_view)


urlpatterns = [
    path('list/', band_list_view, name="bands"),
    path('detail/<int:id>', band_detail_view, name="b_detail"),
    path('a_detail/<int:id>', album_detail_view, name="a_detail"),
    path('create/', band_create_view, name="b_create"),
]