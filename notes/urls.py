from django.urls import path
from . import views



urlpatterns = [

    # Dashboard
    path('', views.dashboard, name='dashboard'),
    # Register
    path('register/', views.register, name='register'),

    path('add-note/', views.add_note, name='add_note'),
    path('edit-note/<int:id>/', views.edit_note, name='edit_note'),
    path('delete-note/<int:id>/', views.delete_note, name='delete_note'),
    path('profile/', views.profile, name='profile'),

    
]