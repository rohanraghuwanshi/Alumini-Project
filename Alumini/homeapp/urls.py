from django.urls import path

from .views import *

app_name = 'homeapp'

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("about-us/", AboutusView.as_view(), name="aboutus"),
    path("contact-us/", ContactView.as_view(), name="contact"),
]
