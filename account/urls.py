from django.urls import path 
from .views import signup, show_profile, edit_profile, user_projects, user_donations, delete_profile
from django.contrib.auth import views

urlpatterns = [
    path('signup/',signup,name='signup'),
    path('logout/',views.LogoutView.as_view,name='logout'),
    path('user-profile', show_profile, name='user_profile'),
    path('edit_profile', edit_profile, name='edit_profile'),
    path('delete-profile', delete_profile, name='delete_profile'),
    path('user-projects', user_projects, name='user_projects'),
    path('user-donations', user_donations, name='user_donations'),

]
