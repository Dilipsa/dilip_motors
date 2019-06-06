from django.urls import path
from . import views
urlpatterns = [
    path('vehicle/', views.car_list, name='car_list'),
    path('vehicle/detail/<int:pk>', views.car_detail, name='car_detail'),
    path('vehicle/new/', views.car_new, name='car_new'),
    path('vehicle/<int:pk>/edit/', views.car_edit, name='car_edit'),
]
