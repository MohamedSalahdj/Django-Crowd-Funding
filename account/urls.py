from django.urls import path 
from .views import signup, show_profile, edit_profile, user_projects, user_donations
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/',signup,name='signup'),
    path('verify_email/',verify_email,name='verify_email'),
    path('activate/<uidb64>/<token>', activate, name='activate'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),    
    path('user-profile', show_profile, name='user_profile'),
    path('edit_profile', edit_profile, name='edit_profile'),
    path('user-projects', user_projects, name='user_projects'),
    path('user-donations', user_donations, name='user_donations'),
    
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),

    path('password-reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password_reset/complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    
    
    

]
