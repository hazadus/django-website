from django.urls import path
from . import views

urlpatterns = [
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('signup_user', views.signup_user, name='signup_user'),
    path('user_profile', views.user_profile, name='user_profile'),
]
