# musician/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_musician, name='add_musician'),
    path('edit/<int:id_no>/', views.edit_musician, name='edit_musician'),
]