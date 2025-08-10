from django.urls import path
from .views import (band_list_view, band_detail_view, band_create_view,
                    album_detail_view, song_detail_view, article_list_view, article_detail_view)


urlpatterns = [
    path('list/', band_list_view, name="bands"),
    path('detail/<int:id>', band_detail_view, name="b_detail"),
    path('a_detail/<int:id>', album_detail_view, name="a_detail"),
    path('s_detail/<int:id>', song_detail_view, name="s_detail"),
    path('create/', band_create_view, name="b_create"),
    path('art_list/', article_list_view, name="articles"),
    path('art_detail/<int:id>', article_detail_view, name="art_detail"),
]