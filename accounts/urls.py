from django.urls import path
from shop import views 
from .views import SignUpView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('create/', SignUpView.as_view(), name='signup'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html", success_url="sent/"), name="password_reset"),
    path('reset_password/sent/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"), name="password_reset_complete"),
    
]

