from . import views
from django.urls import path

app_name = 'chatapp'

urlpatterns = [
    path('', views.chats, name='chats'),
    path('<str:room_name>/', views.chatroom, name='chatroom'),
]
