from django.urls import path
from . import views

urlpatterns = [
    path('branch/', views.branch_detail, name='branch_detail'),
]
