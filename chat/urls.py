from django.contrib import admin
from django.urls import path
from.views import *


urlpatterns = [
    path('chat',chat,name='chat'),
    path('create_room',create_room,name='create_room'),
    path('get_room',get_roomss,name='get_room'),
    path('view_message/<int:id>',view_message,name='view_message'),
    # path('get_room',get_room,name='get_room')
    # path('chat/chat-rooms/', ChatRoomViewSet.as_view({'post': 'create'})),
    # path('chat/chat-messages/', ChatMessageViewSet.as_view({'post': 'create'})),
]