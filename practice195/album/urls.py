# album/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddAlbumCreateView.as_view(), name='add_album'),
    path('edit/<int:id_no>/', views.EditAlbumView.as_view(), name='edit_album'),
    path('delete/<int:id_no>', views.DeleteAlbumView.as_view(), name='delete_entry'),
]