from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('', views.dashboard, name='dashboard'),
    # Register
    path('register/', views.register, name='register'),
    path('add-note/', views.add_note, name='add_note'),
    path('note/<int:id>/', views.note_detail, name='note_detail'),
    path('edit-note/<int:id>/', views.edit_note, name='edit_note'),
    path('delete-note/<int:id>/', views.delete_note, name='delete_note'),
    path('profile/', views.profile, name='profile'),

    
]