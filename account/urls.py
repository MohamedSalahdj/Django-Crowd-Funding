from django.urls import path 
from .views import *
from django.contrib.auth import views

urlpatterns = [
    path('signup/',signup,name='signup'),
    path('verify_email/',verify_email,name='verify_email'),
    path('activate/<uidb64>/<token>', activate, name='activate'),    
    path('logout/',views.LogoutView.as_view,name='logout'),
    path('user-profile', show_profile, name='user_profile'),
    path('edit_profile', edit_profile, name='edit_profile'),
    path('delete-profile', delete_profile, name='delete_profile'),
    path('user-projects', user_projects, name='user_projects'),
    path('user-donations', user_donations, name='user_donations'),

]
