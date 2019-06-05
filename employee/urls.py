from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('detail/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('add/', views.employee_new, name='employee_new'),

]
