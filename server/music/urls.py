from django.urls import path
from .views import band_list_view, band_detail_view, band_create_view


urlpatterns = [
    path('list/', band_list_view, name="bands"),
    path('detail/<int:id>', band_detail_view, name="b_detail"),
    path('create/', band_create_view, name="b_create"),
]