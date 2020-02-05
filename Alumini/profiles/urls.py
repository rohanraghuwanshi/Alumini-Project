from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import *

app_name = 'profiles'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path("registration/", UserRegistrationView.as_view(), name="registration"),
    path('logout/', LogoutView.as_view(), name='logout'),
]
