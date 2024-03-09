from django.urls import path 
from .views import signup
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/',signup,name='signup'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),

    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),

    path('password-reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password_reset/complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    
    
    
]
